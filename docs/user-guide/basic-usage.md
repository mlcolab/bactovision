# Basic Usage

This guide covers the fundamental operations for using BactoVision to analyze bacterial growth images.

## Getting Started

To begin using BactoVision, you need to import the main widget class and create an instance with your image:

```python
from bactovision.widget import BactoWidget

# Create a widget with an image
widget = BactoWidget('path/to/your/image.png')

# Display the widget
widget
```

## Loading Images

BactoVision supports various ways to load images:

```python
# From a file path
widget = BactoWidget('path/to/image.png')

# From a NumPy array
import numpy as np
from PIL import Image

img = np.array(Image.open('path/to/image.png'))
widget = BactoWidget(img)
```

## Basic Annotation Workflow

Once your image is loaded, a typical analysis workflow includes:

### 1. Adjusting the Grid

Set up the grid to match your experimental layout:

```python
# Access and modify grid properties
widget.canvas_widget.grid_num_x = 10  # Number of horizontal grid cells
widget.canvas_widget.grid_num_y = 8   # Number of vertical grid cells
```

You can also use the grid controls in the UI to adjust the grid layout interactively.

### 2. Preprocessing the Image

Enhance image quality for better annotation:

```python
# You can toggle preprocessing options through the UI
# Or programmatically:
widget.clahe_btn.value = True  # Enable CLAHE enhancement
widget.clahe_limit_slider.value = 150  # Set CLAHE limit
widget.subtract_background_btn.value = True  # Enable background subtraction
```

### 3. Annotation

BactoVision provides automatic and manual annotation methods:

#### Automatic Annotation

```python
# Configure auto-annotation parameters
widget.threshold_slider.value = 1.2  # Adjust brightness threshold
widget.small_object_size.value = 0.8  # Set minimum object size

# Run auto-annotation
widget.apply_auto_annotation()
```

You can also use the "Apply auto" button in the UI.

#### Manual Annotation

For manual annotation, use the UI controls:

1. Select annotation mode: "Add" or "Erase"
2. Adjust brush size using the slider
3. Draw or erase on the image by clicking and dragging

### 4. Extracting Data

After annotation, you can extract metrics:

```python
# Get summary metrics from the annotated image
metrics = widget.get_metrics()

# Available metrics include:
# - average_opacity: Average opacity within each grid cell
# - integral_opacity: Total opacity within each grid cell
# - relative_area: Proportion of each grid cell that is annotated
# - num_pixels: Number of annotated pixels in each grid cell

import matplotlib.pyplot as plt

# Visualize metrics
plt.figure(figsize=(10, 6))
plt.imshow(metrics['integral_opacity'])
plt.colorbar()
plt.title('Integral Opacity by Grid Cell')
plt.show()
```

## Saving Results

While BactoVision does not directly save results, you can extract and save the annotation data:

```python
# Get the annotation mask
mask = widget.mask

# Save the mask
from PIL import Image
Image.fromarray((mask * 255).astype('uint8')).save('annotation.png')

# Save metrics to CSV
import pandas as pd
import numpy as np

metrics = widget.get_metrics()
df = pd.DataFrame({
    'integral_opacity': metrics['integral_opacity'].flatten(),
    'average_opacity': metrics['average_opacity'].flatten(),
    'relative_area': metrics['relative_area'].flatten(),
})
df.to_csv('metrics.csv')
```

## Next Steps

For more detailed information about specific features, explore the other guides:

- [Widget Interface](widget-interface.md) for UI details
- [Annotations](annotations.md) for advanced annotation techniques
- [Grid System](grid.md) for detailed grid configuration 