# BactoVision

![BactoVision](images/bactovision-logo.png){ align=right width=300 }

## A Jupyter widget for annotating and visualizing bacterial growth data

BactoVision provides an interactive widget for Jupyter notebook designed for fast semi-automated annotation of bacterial growth images. It combines intuitive manual drawing tools with automatic detection algorithms to make the annotation process efficient and accurate.

BactoVision is used in the paper:

_Tyrosine auxotrophy shapes Staphylococcus aureus nasal colonization and interactions with commensal communities_ L. Camus et al. 2025 (submitted)

## Key Features

- **Jupyter integration** - Annotate data directly in Jupyter notebook to enable flexiblility and integration with other methods
- **Interactive annotation** - Combine automatic and manual annotation methods
- **Grid system** - Analyze data in a structured grid format
- **Image enhancement** - Apply CLAHE and other image processing techniques
- **Quantitative analysis** - Extract metrics on bacterial growth
- **Intuitive interface** - Simple and user-friendly design

## Quick Start

```python
from bactovision import BactoWidget

# Create a widget with an image
widget = BactoWidget('path/to/image.png')

# Display the widget
widget
```

To get the mask and the metrics after the annotation is completed, run:

```python
annotation_mask = widget.get_annotation_mask()
metrics = widget.get_metrics()
```

## Citation

If you use BactoVision in your research, please cite:

```
Camus L. et al. (2025). Tyrosine auxotrophy shapes Staphylococcus aureus nasal colonization
and interactions with commensal communities. [Journal pending].
```
