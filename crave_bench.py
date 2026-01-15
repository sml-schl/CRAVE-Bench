"""
CRAVE-Bench Dataset Loader

A simple Python interface for loading and working with the CRAVE-Bench dataset.

Usage:
    from crave_bench import CRAVEBench
    
    dataset = CRAVEBench("path/to/crave-bench")
    
    # Load all images
    all_images = dataset.load_all()
    
    # Load by stratum
    consensus = dataset.load_stratum("consensus")
    divergence = dataset.load_stratum("divergence")
    outliers = dataset.load_stratum("outlier")
    
    # Get metadata for an image
    metadata = dataset.get_metadata("divergence_001")
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any, Iterator
from dataclasses import dataclass


@dataclass
class CRAVEImage:
    """Represents a single image in the CRAVE-Bench dataset."""
    id: str
    filename: str
    stratum: str
    edge_case_type: str
    image_path: Path
    metadata: Dict[str, Any]
    
    def load_image(self):
        """Load the image using PIL. Returns PIL.Image object."""
        try:
            from PIL import Image
            return Image.open(self.image_path)
        except ImportError:
            raise ImportError("PIL/Pillow is required to load images. Install with: pip install Pillow")
    
    @property
    def ground_truth(self) -> Optional[Dict[str, Any]]:
        """Get ground truth information for this image."""
        return self.metadata.get("ground_truth")
    
    @property
    def text_overlay(self) -> Optional[str]:
        """Get the text overlay content for this image."""
        return self.metadata.get("text_overlay")
    
    @property 
    def cultural_dimensions(self) -> Optional[Dict[str, str]]:
        """Get cultural dimension annotations (divergence stratum only)."""
        return self.metadata.get("cultural_dimensions")
    
    @property
    def vulnerability_tested(self) -> Optional[str]:
        """Get the vulnerability being tested (outlier stratum only)."""
        return self.metadata.get("vulnerability_tested")


class CRAVEBench:
    """
    CRAVE-Bench Dataset Loader
    
    Cultural Relativity Assessment for Visual Expression Benchmark
    
    A synthetic multimodal benchmark for evaluating cross-cultural bias
    in vision-language models for hateful meme detection.
    """
    
    STRATA = ["consensus", "divergence", "outlier"]
    
    def __init__(self, dataset_path: str):
        """
        Initialize the CRAVE-Bench loader.
        
        Args:
            dataset_path: Path to the CRAVE-Bench dataset directory
        """
        self.dataset_path = Path(dataset_path)
        self.annotations_path = self.dataset_path / "annotations.json"
        
        if not self.annotations_path.exists():
            raise FileNotFoundError(
                f"annotations.json not found at {self.annotations_path}. "
                "Please ensure you have the complete CRAVE-Bench dataset."
            )
        
        with open(self.annotations_path, "r") as f:
            self._annotations = json.load(f)
        
        self._image_index = {
            img["id"]: img for img in self._annotations["images"]
        }
    
    @property
    def version(self) -> str:
        """Get dataset version."""
        return self._annotations.get("version", "unknown")
    
    @property
    def total_images(self) -> int:
        """Get total number of images in the dataset."""
        return len(self._annotations["images"])
    
    @property
    def strata_summary(self) -> Dict[str, Dict]:
        """Get summary statistics for each stratum."""
        return self._annotations.get("strata", {})
    
    def _resolve_image_path(self, image_meta: Dict) -> Path:
        """Resolve the full path to an image file."""
        stratum = image_meta["stratum"]
        filename = image_meta["filename"]
        
        # Handle consensus sub-directories
        if stratum == "consensus":
            ground_truth = image_meta.get("ground_truth", {})
            if isinstance(ground_truth, dict):
                label = ground_truth.get("universal", "not_hateful")
            else:
                label = ground_truth if ground_truth else "not_hateful"
            
            if label == "hateful":
                return self.dataset_path / "consensus" / "hate" / filename
            else:
                return self.dataset_path / "consensus" / "not_hate" / filename
        else:
            return self.dataset_path / stratum / filename
    
    def _create_crave_image(self, image_meta: Dict) -> CRAVEImage:
        """Create a CRAVEImage object from metadata."""
        return CRAVEImage(
            id=image_meta["id"],
            filename=image_meta["filename"],
            stratum=image_meta["stratum"],
            edge_case_type=image_meta.get("edge_case_type", "unknown"),
            image_path=self._resolve_image_path(image_meta),
            metadata=image_meta
        )
    
    def load_all(self) -> List[CRAVEImage]:
        """
        Load all images in the dataset.
        
        Returns:
            List of CRAVEImage objects
        """
        return [
            self._create_crave_image(img) 
            for img in self._annotations["images"]
        ]
    
    def load_stratum(self, stratum: str) -> List[CRAVEImage]:
        """
        Load all images from a specific stratum.
        
        Args:
            stratum: One of "consensus", "divergence", or "outlier"
            
        Returns:
            List of CRAVEImage objects from the specified stratum
        """
        if stratum not in self.STRATA:
            raise ValueError(
                f"Unknown stratum '{stratum}'. Must be one of: {self.STRATA}"
            )
        
        return [
            self._create_crave_image(img)
            for img in self._annotations["images"]
            if img["stratum"] == stratum
        ]
    
    def load_consensus_hate(self) -> List[CRAVEImage]:
        """Load consensus hateful images."""
        return [
            img for img in self.load_stratum("consensus")
            if img.ground_truth and img.ground_truth.get("universal") == "hateful"
        ]
    
    def load_consensus_not_hate(self) -> List[CRAVEImage]:
        """Load consensus non-hateful images."""
        return [
            img for img in self.load_stratum("consensus")
            if img.ground_truth and img.ground_truth.get("universal") == "not_hateful"
        ]
    
    def get_image(self, image_id: str) -> Optional[CRAVEImage]:
        """
        Get a specific image by ID.
        
        Args:
            image_id: The unique identifier for the image (e.g., "divergence_001")
            
        Returns:
            CRAVEImage object or None if not found
        """
        if image_id in self._image_index:
            return self._create_crave_image(self._image_index[image_id])
        return None
    
    def get_metadata(self, image_id: str) -> Optional[Dict[str, Any]]:
        """
        Get raw metadata for an image.
        
        Args:
            image_id: The unique identifier for the image
            
        Returns:
            Dictionary of metadata or None if not found
        """
        return self._image_index.get(image_id)
    
    def get_missing_images(self) -> List[Dict[str, Any]]:
        """
        Get information about images that could not be generated.
        
        Returns:
            List of dictionaries describing missing images and reasons
        """
        return self._annotations.get("missing_images", [])
    
    def iter_images(self, stratum: Optional[str] = None) -> Iterator[CRAVEImage]:
        """
        Iterate over images in the dataset.
        
        Args:
            stratum: Optional stratum filter
            
        Yields:
            CRAVEImage objects
        """
        images = self.load_stratum(stratum) if stratum else self.load_all()
        for img in images:
            yield img
    
    def __len__(self) -> int:
        return self.total_images
    
    def __repr__(self) -> str:
        return (
            f"CRAVEBench(version={self.version}, "
            f"total_images={self.total_images}, "
            f"path={self.dataset_path})"
        )


# Convenience function for quick loading
def load_crave_bench(path: str) -> CRAVEBench:
    """
    Load the CRAVE-Bench dataset.
    
    Args:
        path: Path to the dataset directory
        
    Returns:
        CRAVEBench dataset loader instance
    """
    return CRAVEBench(path)


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        dataset_path = sys.argv[1]
    else:
        dataset_path = "."
    
    print("Loading CRAVE-Bench dataset...")
    dataset = CRAVEBench(dataset_path)
    
    print(f"\n{dataset}")
    print(f"\nStrata Summary:")
    for stratum, info in dataset.strata_summary.items():
        print(f"  {stratum}: {info}")
    
    print(f"\nMissing Images (generation refused):")
    for missing in dataset.get_missing_images():
        print(f"  - {missing['id']}: {missing['reason']}")
    
    print("\nSample images by stratum:")
    for stratum in dataset.STRATA:
        images = dataset.load_stratum(stratum)
        print(f"\n  {stratum.upper()} ({len(images)} images):")
        for img in images[:2]:
            print(f"    - {img.id}: {img.edge_case_type}")
        if len(images) > 2:
            print(f"    ... and {len(images) - 2} more")
