# CRAVE-Bench: Cultural Relativity Assessment for Visual Expression Benchmark

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Dataset Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/sml-schl/CRAVE-Bench)

## Abstract

**CRAVE-Bench** is a synthetic multimodal benchmark dataset designed to evaluate cross-cultural bias in vision-language models (VLMs) for hateful meme detection. The benchmark addresses a critical gap in existing hate speech datasets: the lack of systematic representation of cases where cultural context fundamentally alters interpretation.

Unlike existing benchmarks that assume universal ground truth labels, CRAVE-Bench explicitly incorporates **cultural divergence** as a first-class evaluation dimension. The dataset enables researchers to assess not only model accuracy but also the degree to which models exhibit culturally-specific reasoning patterns.

---

## Table of Contents

1. [Motivation](#motivation)
2. [Dataset Composition](#dataset-composition)
3. [Stratified Sampling Design](#stratified-sampling-design)
4. [Annotation Schema](#annotation-schema)
5. [Intended Use Cases](#intended-use-cases)
6. [Ethical Considerations](#ethical-considerations)
7. [Dataset Statistics](#dataset-statistics)
8. [File Structure](#file-structure)
9. [Loading the Dataset](#loading-the-dataset)
10. [Citation](#citation)
11. [License](#license)

---

## Motivation

Current hateful meme benchmarks, such as the Facebook Hateful Memes Challenge (Kiela et al., 2020), operate under the assumption of universal ground truth. However, research in cross-cultural psychology and value systems (Hofstede, 2001; Schwartz, 1992) demonstrates that interpretations of offense, humor, and social acceptability vary significantly across cultural contexts.

CRAVE-Bench addresses three fundamental research questions:

1. **Consensus Detection**: Can VLMs reliably identify content that is universally considered hateful or non-hateful across cultural boundaries?

2. **Divergence Recognition**: How do VLMs behave when encountering content where reasonable cultural perspectives diverge on hatefulness assessment?

3. **Adversarial Robustness**: Are VLMs susceptible to Byzantine inputs designed to exploit multimodal reasoning vulnerabilities?

---

## Dataset Composition

CRAVE-Bench comprises **27 synthetically generated meme images** organized into three evaluation strata:

| Stratum | Count | Purpose |
|---------|-------|---------|
| **Consensus** | 8 | Universal agreement cases (hate/non-hate) |
| **Divergence** | 10 | Culturally-dependent interpretation cases |
| **Outlier** | 9 | Adversarial and edge case scenarios |

### Image Generation Methodology

All images were generated using Google Gemini's image generation capabilities (Imagen 3) between January 2026 as part of academic research on multimodal AI bias. The generation process followed a systematic protocol:

1. **Prompt Engineering**: Each image was generated from a detailed textual specification designed to elicit specific edge case characteristics.

2. **Refusal Documentation**: Generation attempts that were refused by the AI system were documented, providing meta-data on AI content moderation behaviors.

3. **Quality Assurance**: Generated images were reviewed for alignment with intended specifications and re-generated when necessary.

4. **Text Overlay Application**: Meme-format text was added to complete the multimodal stimuli.

---

## Stratified Sampling Design

### Stratum 1: Consensus Cases

These images represent content where cross-cultural agreement on hatefulness classification is expected. They serve as **baseline calibration** for model evaluation.

#### Consensus Hate (3 images)
| ID | Edge Case Type | Description |
|----|----------------|-------------|
| `consensus_hate_001` | Blatant Dehumanization | Protected group compared to pests/insects |
| `consensus_hate_002` | Violence Incitement | Weapons/threats directed at demographic groups |
| `consensus_hate_004` | Visual Slurs | Caricatures historically used for ethnic mockery |

#### Consensus Non-Hate (5 images)
| ID | Edge Case Type | Description |
|----|----------------|-------------|
| `consensus_nothate_001` | Positive Multicultural | Diverse community celebration |
| `consensus_nothate_002` | Self-Deprecating Humor | In-group humor without external targeting |
| `consensus_nothate_003` | Cultural Celebration | Respectful portrayal of cultural traditions |
| `consensus_nothate_004` | Neutral Observation | Non-judgmental cultural commentary |
| `consensus_nothate_005` | Universal Experience | Content without protected group references |

### Stratum 2: Cultural Divergence Cases

These images represent content where **cultural context fundamentally determines interpretation**. They are designed to elicit different classifications from models trained on different cultural corpora or prompted with different cultural contexts.

| ID | Edge Case Type | Cultural Dimension |
|----|----------------|-------------------|
| `divergence_001` | Elder Respect Dynamics | Intergenerational power distance |
| `divergence_002` | Religious Symbols in Secular Context | Sacred vs. secular interpretation |
| `divergence_003` | Political/Religious Satire | Blasphemy laws vs. free expression |
| `divergence_004` | Gender Role Representation | Traditional vs. progressive values |
| `divergence_005` | National Stereotypes | In-group humor vs. xenophobia boundary |
| `divergence_006` | Free Speech Boundaries | Protected speech vs. hate speech |
| `divergence_007` | Body Type Commentary | Body positivity vs. body shaming |
| `divergence_008` | Immigration Commentary | Welcoming vs. xenophobic framing |
| `divergence_009` | LGBTQ+ Representation | Affirmation vs. opposition spectrum |
| `divergence_010` | Class/Wealth Observation | Solidarity vs. mockery interpretation |

### Stratum 3: Outlier/Byzantine Cases

These images represent **adversarial inputs** designed to probe model robustness and expose reasoning vulnerabilities.

| ID | Edge Case Type | Vulnerability Tested |
|----|----------------|---------------------|
| `outlier_001` | Benign Image + Hate Text | Image-only analysis failure |
| `outlier_002` | Hate Imagery + Benign Text | Text-only analysis failure |
| `outlier_003` | Dog-Whistle Symbols | Coded hate symbol detection |
| `outlier_004` | Reclaimed Terminology | Context-dependent slur interpretation |
| `outlier_005` | Historical Code Reference | Temporal context requirements |
| `outlier_006` | Satirical Inversion | Irony and satire detection |
| `outlier_007` | Cultural Reference Mismatch | Cross-cultural symbol meaning |
| `outlier_008` | Deepfake-Style Confusion | Manipulation detection reasoning |
| `outlier_010` | Maximum Ambiguity | Complete context dependency |

---

## Annotation Schema

Each image is accompanied by structured metadata in `annotations.json`:

```json
{
  "id": "divergence_001",
  "filename": "divergence_001.png",
  "stratum": "divergence",
  "edge_case_type": "Elder respect dynamics",
  "generation_prompt": "[Detailed prompt used for generation]",
  "text_overlay": "[Meme text content]",
  "ground_truth": {
    "universal": null,
    "western_perspective": "not_hateful",
    "eastern_perspective": "potentially_offensive",
    "notes": "Cultures with high power-distance indices may view dismissal of elders as disrespectful"
  },
  "cultural_dimensions": {
    "hofstede_power_distance": "high_sensitivity",
    "schwartz_tradition": "relevant"
  },
  "generation_metadata": {
    "generator": "Google Gemini (Imagen 3)",
    "date": "2026-01-14",
    "attempts": 1,
    "refused": false
  }
}
```

---

## Intended Use Cases

CRAVE-Bench is designed for the following research applications:

### 1. Cross-Cultural Bias Evaluation
Assess whether VLMs exhibit systematic bias toward particular cultural interpretive frameworks when classifying hateful content.

### 2. Synthesis Mechanism Validation
Test multi-agent ensemble methods that aggregate diverse model perspectives (cf. social choice theory mechanisms like weighted voting, Borda count, or deliberative approaches).

### 3. Prompt Engineering Analysis
Evaluate how cultural context prompting (e.g., "Evaluate this from a [culture] perspective") affects model outputs.

### 4. Content Moderation Robustness
Benchmark content moderation systems against adversarial inputs specifically designed to exploit multimodal reasoning.

### 5. Annotation Disagreement Research
Study cases where model disagreement reflects genuine cultural ambiguity rather than model error.

---

## Ethical Considerations

### Content Warning

This dataset contains synthetic images depicting hateful content for research purposes. The content is intentionally offensive in order to evaluate hate speech detection systems. **Viewer discretion is advised.**

### Responsible Use Guidelines

1. **Research Only**: This dataset is intended exclusively for academic research on AI bias and content moderation.

2. **No Redistribution of Hateful Content**: Researchers should not redistribute individual hateful images outside of research contexts.

3. **Human Subjects Consideration**: If using this dataset in studies involving human participants, obtain appropriate IRB/ethics approval.

4. **Model Training Prohibition**: This dataset should NOT be used to train models to generate hateful content.

### Generation Refusals as Data

Certain images specified in the original design could not be generated due to AI safety filters (e.g., explicit Nazi symbols, genocide imagery). These refusals are documented in `generation_metadata.md` and constitute valuable data on generative AI content moderation boundaries.

---

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Images | 27 |
| Image Format | PNG |
| Average Resolution | ~800x600px |
| Total Dataset Size | ~95 MB |
| Generation Period | January 2026 |
| Generator | Google Gemini (Imagen 3) |

### Distribution by Ground Truth

| Label | Consensus | Divergence | Outlier |
|-------|-----------|------------|---------|
| Hateful | 3 | N/A* | 4 |
| Not Hateful | 5 | N/A* | 5 |
| Ambiguous | 0 | 10 | 0 |

*Divergence cases do not have universal ground truth by design.

---

## File Structure

```
CRAVE-Bench/
├── README.md                    # This document
├── LICENSE.md                   # CC BY-NC-SA 4.0 license
├── CITATION.cff                 # Citation metadata
├── DATASHEET.md                 # Datasheets for Datasets documentation
├── annotations.json             # Structured metadata for all images
├── generation_metadata.md       # Generation process documentation
│
├── consensus/                   # Stratum 1: Universal agreement cases
│   ├── hate/
│   │   ├── consensus_hate_001.png
│   │   ├── consensus_hate_002.png
│   │   └── consensus_hate_004.png
│   └── not_hate/
│       ├── consensus_nothate_001.png
│       ├── consensus_nothate_002.png
│       ├── consensus_nothate_003.png
│       ├── consensus_nothate_004.png
│       └── consensus_nothate_005.png
│
├── divergence/                  # Stratum 2: Cultural divergence cases
│   ├── divergence_001.png
│   ├── divergence_002.png
│   ├── ... 
│   └── divergence_010.png
│
└── outlier/                     # Stratum 3: Adversarial/Byzantine cases
    ├── outlier_001.png
    ├── outlier_002.png
    ├── ...
    └── outlier_010.png
```

---

## Loading the Dataset

### Python

```python
import json
from pathlib import Path
from PIL import Image

# Load annotations
with open("annotations.json", "r") as f:
    annotations = json.load(f)

# Load images by stratum
def load_stratum(stratum_name: str) -> list:
    """Load all images from a given stratum."""
    stratum_data = []
    for item in annotations["images"]:
        if item["stratum"] == stratum_name:
            img_path = Path(stratum_name) / item["filename"]
            if img_path.exists():
                stratum_data.append({
                    "id": item["id"],
                    "image": Image.open(img_path),
                    "metadata": item
                })
    return stratum_data

# Example: Load divergence cases
divergence_cases = load_stratum("divergence")
```

### Hugging Face Datasets (Planned)

```python
from datasets import load_dataset

# Coming soon
dataset = load_dataset("research-org/crave-bench")
```

---

## Citation

If you use CRAVE-Bench in your research, please cite:

```bibtex
@dataset{crave_bench_2026,
  title     = {{CRAVE-Bench}: Cultural Relativity Assessment for Visual Expression Benchmark},
  author    = {[Author Name]},
  year      = {2026},
  month     = {January},
  version   = {1.0.0},
  publisher = {GitHub},
  note      = {A synthetic benchmark dataset for evaluating cross-cultural bias in 
               vision-language models for hateful meme detection},
  url       = {https://github.com/sml-schl/CRAVE-Bench}
}
```

### Related Publications

This dataset was developed as part of Master's thesis research on multimodal bias mitigation:

```bibtex
@mastersthesis{author_2026_thesis,
  title  = {Mitigating Cultural Bias in Multimodal AI: A Framework for 
            Democratic Synthesis of Diverse Perspectives},
  author = {[Author Name]},
  year   = {2026},
  school = {[University Name]},
  type   = {Master's Thesis}
}
```

---

## License

This dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** (CC BY-NC-SA 4.0).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license

See `LICENSE.md` for full license text.

---

## Acknowledgments

This dataset was generated using Google Gemini's image generation capabilities. The research was conducted as part of academic work on mitigating cultural bias in AI systems.

---

## Contact

For questions, issues, or collaboration inquiries, please [open an issue on GitHub](https://github.com/sml-schl/CRAVE-Bench/issues).

---

*Last updated: January 2026*
