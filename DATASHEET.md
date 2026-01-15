# Datasheet for CRAVE-Bench

*Following the "Datasheets for Datasets" framework (Gebru et al., 2021)*

---

## Motivation

### For what purpose was the dataset created?

CRAVE-Bench was created to address a critical gap in existing hateful meme benchmarks: the lack of systematic representation of cases where cultural context fundamentally alters interpretation. The dataset enables researchers to evaluate cross-cultural bias in vision-language models and test synthesis mechanisms that aggregate diverse cultural perspectives.

### Who created the dataset and on behalf of which entity?

The dataset was created as part of Master's thesis research on "Mitigating Cultural Bias in Multimodal AI" at [University Name]. The work was conducted independently under academic supervision.

### Who funded the creation of the dataset?

This was unfunded academic research conducted as part of a Master's degree program.

---

## Composition

### What do the instances that comprise the dataset represent?

Each instance is a synthetically generated meme image (PNG format) with accompanying metadata. The images are designed to represent edge cases in hateful content detection where cultural context plays a significant role.

### How many instances are there in total?

27 images organized into three strata:
- **Consensus**: 8 images (3 hateful, 5 non-hateful)
- **Divergence**: 10 images (culturally ambiguous)
- **Outlier**: 9 images (4 hateful, 5 non-hateful in Western context)

### Does the dataset contain all possible instances or is it a sample?

The dataset is a purposefully constructed sample designed to cover specific edge case categories. It is not intended to be exhaustive but rather to provide targeted probes for model evaluation.

### What data does each instance consist of?

Each instance consists of:
1. **Image file** (PNG, ~800x600px average)
2. **Structured metadata** including:
   - Unique identifier
   - Stratum classification
   - Edge case type
   - Generation prompt
   - Text overlay content
   - Ground truth labels (where applicable)
   - Cultural dimension annotations

### Is there a label or target associated with each instance?

Yes, but the labeling scheme varies by stratum:
- **Consensus**: Binary labels (hateful/not_hateful) with expected universal agreement
- **Divergence**: No universal label; multiple perspective-dependent labels provided
- **Outlier**: Binary labels based on intended classification challenge

### Is any information missing from individual instances?

Three images from the original 30-image design could not be generated due to AI safety filters:
- `consensus_hate_003` (historical hate symbols)
- `consensus_hate_005` (genocide reference)
- `outlier_009` (positive message + problematic imagery)

These refusals are documented as valuable meta-data on generative AI content moderation.

### Are relationships between individual instances made explicit?

Yes. Instances within each stratum share structural properties that define that stratum. Variant images (e.g., `divergence_001.png` and `divergence_001-2.png`) represent multiple generation attempts for the same specification.

### Are there any errors, sources of noise, or redundancies?

- Some images have multiple variants (indicated by `-2`, `-3` suffixes) where regeneration was needed
- Text overlays may contain minor typographical irregularities due to generation model limitations
- Image quality varies depending on generation complexity

### Is the dataset self-contained?

Yes. All necessary files are included in the repository.

---

## Collection Process

### How was the data associated with each instance acquired?

All images were synthetically generated using Google Gemini's image generation capabilities (Imagen 3) via the Gemini API during January 2026.

### What mechanisms or procedures were used to collect the data?

1. **Specification Development**: Detailed prompts were designed for each edge case type based on literature review of cultural bias in content moderation
2. **Generation Execution**: Prompts were submitted to Google Gemini with a standard ethical research preamble
3. **Quality Review**: Generated images were reviewed for alignment with specifications
4. **Regeneration**: Non-compliant images were regenerated with adjusted prompts
5. **Text Overlay**: Meme-format text was added using image editing tools

### If the dataset is a sample from a larger set, what was the sampling strategy?

Not applicable—this is a purposefully constructed dataset, not a sample.

### Who was involved in the data collection process?

The dataset was created by a single researcher (the thesis author) under academic supervision.

### Over what timeframe was the data collected?

Generation occurred between January 4-15, 2026.

### Were any ethical review processes conducted?

The research was conducted under the ethical guidelines of the host institution. Given that the dataset is entirely synthetic (no real human subjects or scraped personal data), formal IRB approval was not required.

---

## Preprocessing/Cleaning/Labeling

### Was any preprocessing/cleaning/labeling of the data done?

1. **Format Standardization**: All images were saved as PNG files
2. **Naming Convention**: Systematic naming (`{stratum}_{type}_{number}.png`)
3. **Metadata Extraction**: Generation details were logged during creation
4. **Text Overlay Application**: Meme text was added post-generation

### Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data?

Some base images (without text overlay) were preserved but are not included in the public release.

### Is the software that was used to preprocess/clean/label the data available?

Generation was performed via Google Gemini API. Text overlays were added using standard image editing tools.

---

## Uses

### Has the dataset been used for any tasks already?

Yes. The dataset was developed for and used in Master's thesis research evaluating cross-cultural bias in multimodal AI systems.

### Is there a repository that links to any or all papers or systems that use the dataset?

Not yet. This is the initial public release.

### What (other) tasks could the dataset be used for?

- Cross-cultural bias evaluation in VLMs
- Content moderation robustness testing
- Multi-agent synthesis mechanism validation
- Prompt engineering effectiveness studies
- Annotation disagreement analysis
- AI safety and alignment research

### Is there anything about the composition of the dataset or the way it was collected that might impact future uses?

1. **Cultural Representation Limitations**: The divergence cases were designed from a primarily Western academic perspective; other cultural dimensions may not be fully represented
2. **Generation Model Bias**: Google Gemini's training data and safety filters influenced what could be generated
3. **Small Scale**: With only 27 images, the dataset is designed for targeted probing rather than statistical power

### Are there tasks for which the dataset should not be used?

- Training models to generate hateful content
- Any commercial content moderation deployment without additional validation
- Psychological research on humans without ethics approval
- Redistribution of hateful images outside research contexts

---

## Distribution

### Will the dataset be distributed to third parties outside of the entity on behalf of which the dataset was created?

Yes. The dataset is intended for public release under CC BY-NC-SA 4.0 license.

### How will the dataset be distributed?

Via GitHub repository and potentially Hugging Face Datasets.

### When will the dataset be distributed?

Initial release: January 2026.

### Will the dataset be distributed under a copyright or other intellectual property (IP) license?

Yes. Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

### Have any third parties imposed IP-based or other restrictions on the data?

Generated images are subject to Google's terms of service for Gemini-generated content.

---

## Maintenance

### Who will be supporting/hosting/maintaining the dataset?

The thesis author will maintain the dataset during the research period. Long-term hosting via institutional repository or Zenodo is planned.

### How can the owner/curator/manager of the dataset be contacted?

Via GitHub issues or the contact information in the repository.

### Is there an erratum?

Not currently. Any corrections will be documented in a CHANGELOG.md file.

### Will the dataset be updated?

Potential updates include:
- Additional images for underrepresented edge cases
- Expanded cultural dimension annotations
- Community-contributed annotations from diverse cultural perspectives

### Will older versions of the dataset continue to be supported?

Yes. Version history will be maintained via semantic versioning.

### If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?

Contributions are welcome via GitHub pull requests. Contributors should follow the established annotation schema and generation documentation standards.

---

## References

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM*, 64(12), 86-92. https://doi.org/10.1145/3458723

Kiela, D., Firooz, H., Mober, A., Goswami, V., Sivakumar, A., Ringshia, P., & Testuggine, D. (2020). The hateful memes challenge: Detecting hate speech in multimodal memes. *Advances in Neural Information Processing Systems*, 33.

Hofstede, G. (2001). *Culture's consequences: Comparing values, behaviors, institutions and organizations across nations*. Sage publications.

Schwartz, S. H. (1992). Universals in the content and structure of values: Theoretical advances and empirical tests in 20 countries. *Advances in Experimental Social Psychology*, 25, 1-65.
