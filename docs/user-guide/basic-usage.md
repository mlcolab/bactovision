# Basic Usage

This guide covers the fundamental operations for using BactoVision to analyze bacterial growth images.

## Getting Started

To begin using BactoVision, you need to import the main widget class and create an instance with your image:

```python
from bactovision.widget import BactoWidget

# Create a widget with an image
widget = BactoWidget('path/to/your/image.png')
```

## Loading Images

BactoVision supports various ways to load images:

```python
# From a file path
widget = BactoWidget('path/to/image.png')

# optionally, one can also provide the grid configuration path:

widget = BactoWidget('path/to/image.png', grid_config='path/to/grid_config.json')

# From a NumPy array
import numpy as np
from PIL import Image

img = np.array(Image.open('path/to/image.png'))
widget = BactoWidget(img)
```

## Grid

Next, one should set the [Grid](grid.md) - either manually or by providing the path to the saved grid configuration.


## Annotation

See the [Annotation](annotation.md) page for details on the annotation process.

## Save metrics

After annotating the image, extract and save the [Metrics](metrics.md).
