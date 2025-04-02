# API Reference

This section provides detailed documentation for BactoVision's API. It covers the main classes and functions that you can use programmatically.

## Package Structure

BactoVision consists of several main components:

- **BactoWidget** (`bactovision.widget.BactoWidget`) - The main widget class
- **CanvasWidget** (`bactovision.canvas_widget.CanvasWidget`) - The underlying canvas implementation
- **Image Processing** (`bactovision.image_processing`) - Image processing utilities

## Core Classes Overview

### BactoWidget

The main user-facing class that integrates all components:

```python
from bactovision.widget import BactoWidget

widget = BactoWidget('path/to/image.png')
```

This class provides:

- Image loading and display
- UI controls for annotation
- Grid configuration
- Metrics extraction

### CanvasWidget

The lower-level widget that handles the canvas rendering and interactions:

```python
from bactovision.canvas_widget import CanvasWidget

canvas = CanvasWidget()
canvas.set_image(image_array)
```

This class provides:

- Image rendering
- Drawing capabilities
- Annotation storage
- Grid implementation

### Image Processing Utilities

A collection of functions for processing bacterial growth images:

```python
from bactovision.image_processing import segment_by_thresholding, normalize_image

# Segment an image
image, mask = segment_by_thresholding(image_array, t=1.0, s=1.0)

# Normalize an image to [0,1] range
normalized_img = normalize_image(image_array)
```

## Detailed API Documentation

Each component has detailed documentation available:

- [BactoWidget](bacto-widget.md) - Main widget documentation
- [CanvasWidget](canvas-widget.md) - Canvas functionality
- [Image Processing](image-processing.md) - Image processing functions

## Usage Examples

For example code showing how to use these APIs, see the [Examples](../examples.md) page.
