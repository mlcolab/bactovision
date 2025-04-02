# Widget Interface

This guide provides a detailed overview of the BactoVision user interface components and their functions.

## Interface Overview

The BactoVision widget is organized into several functional sections:

![BactoVision Interface](../images/widget-interface.png)

The interface consists of:

1. **Control Panel** - Contains all the adjustment controls
2. **Canvas** - The main display and interaction area

## Control Panel

The Control Panel is divided into two main columns:

### Preprocessing Column

#### Grid Controls

![Grid Controls](../images/grid-controls.png)

- **Adjust Grid** toggle - Enables grid adjustment mode
- **Hide Grid** toggle - Shows/hides the grid overlay
- **Horizontal/Vertical Grid Size** sliders - Control the number of grid cells
- **Padding Sliders** (accessible when "Adjust Grid" is on) - Control the margins around the grid

#### Image Enhancement Controls

![Enhancement Controls](../images/enhancement-controls.png)

- **Apply CLAHE** toggle - Enables Contrast Limited Adaptive Histogram Equalization
- **CLAHE Limit** slider - Controls the contrast enhancement strength
- **Subtract Background** toggle - Removes estimated background intensity
- **Colormap** dropdown - Changes the color scheme for visualizing the image

### Annotation Column

#### Manual Annotation Controls

![Manual Annotation](../images/manual-annotation.png)

- **Manual Annotation** toggle buttons - Switch between modes:
  - **Off** - Disables manual annotation
  - **Add** - Enables drawing annotations
  - **Erase** - Enables erasing annotations
- **Brush Size** slider - Controls the size of the annotation brush

#### Automatic Annotation Controls

![Auto Annotation](../images/auto-annotation.png)

- **Apply Auto** button - Runs automatic annotation
- **Hide Annotation** toggle - Shows/hides annotations
- **Brightness Threshold** slider - Controls the threshold for automatic detection
- **Smallest Size** slider - Sets the minimum size for detected objects

## Canvas

![Canvas](../images/canvas.png)

The canvas is the main area where:

- The bacterial growth image is displayed
- Grid lines are shown (when not hidden)
- Manual annotations can be drawn (when in Add or Erase mode)
- Results of automatic annotation are displayed

### Canvas Interactions

- **Left-click and drag** - Draw or erase annotations (depending on the selected mode)
- **Mouse wheel** - Zoom in/out (if supported by your Jupyter environment)
- **Click and drag grid lines** - Adjust grid positions (when "Adjust Grid" is enabled)

## Programmatic Control

All interface elements can also be controlled programmatically:

```python
# Grid controls
widget.change_grid_btn.value = True  # Enable grid adjustment
widget.hide_grid_btn.value = False  # Show grid
widget.x_grid_size_slider.value = 10  # Set horizontal grid size
widget.y_grid_size_slider.value = 8  # Set vertical grid size

# Image enhancement
widget.clahe_btn.value = True  # Enable CLAHE
widget.clahe_limit_slider.value = 150  # Set CLAHE limit
widget.subtract_background_btn.value = True  # Enable background subtraction
widget.cmap_down.value = 'viridis'  # Change colormap

# Manual annotation
widget.draw_mode_btns.value = 'Add'  # Set annotation mode
widget.brush_size_slider.value = 5  # Set brush size

# Automatic annotation
widget.threshold_slider.value = 1.2  # Set brightness threshold
widget.small_object_size.value = 0.8  # Set minimum object size
widget.hide_annotation_btn.value = False  # Show annotations
```

## Accessing Canvas Data

You can access the raw data from the canvas:

```python
# Get current annotation mask
mask = widget.mask

# Get grid dimensions
grid_info = widget.canvas_widget.get_grid_dict()
print(f"Grid: {grid_info['num_x']} x {grid_info['num_y']}")

# Get processed image
processed_img = widget._preprocessed_img
```

## Additional Views

BactoVision does not provide multiple views of the same data. However, you can create separate visualizations using the extracted data:

```python
import matplotlib.pyplot as plt
import numpy as np

# Visualize the mask
plt.figure(figsize=(8, 6))
plt.imshow(widget.mask, cmap='gray')
plt.title('Annotation Mask')
plt.colorbar()
plt.show()

# Visualize metrics
metrics = widget.get_metrics()
plt.figure(figsize=(8, 6))
plt.imshow(metrics['integral_opacity'])
plt.title('Integral Opacity')
plt.colorbar()
plt.show()
``` 