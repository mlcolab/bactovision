# BactoWidget API

The `BactoWidget` class is the main user interface component of BactoVision. It integrates all functionality into a single widget that can be used in Jupyter notebooks.

```python
from bactovision.widget import BactoWidget
```

## Class Constructor

```python
BactoWidget(img, mask=None)
```

### Parameters

- **img** (`numpy.ndarray` or `str` or `pathlib.Path`): The image to be processed. Can be either a NumPy array or a path to an image file.
- **mask** (`numpy.ndarray`, optional): A pre-existing annotation mask. Default is `None`.

### Returns

A BactoWidget instance that can be displayed in a Jupyter notebook.

### Example

```python
# Create from file path
widget = BactoWidget('path/to/image.png')

# Create from NumPy array
import numpy as np
from PIL import Image
image_array = np.array(Image.open('path/to/image.png'))
widget = BactoWidget(image_array)

# With a pre-existing mask
mask = np.zeros_like(image_array[:,:,0])
mask[100:200, 100:200] = 1  # Example annotation
widget = BactoWidget(image_array, mask=mask)
```

## Properties

### UI Controls

#### Grid Controls

- **change_grid_btn** (`ipywidgets.ToggleButton`): Toggle button to enable/disable grid adjustment mode.
- **hide_grid_btn** (`ipywidgets.ToggleButton`): Toggle button to show/hide the grid.
- **x_grid_size_slider** (`ipywidgets.IntSlider`): Slider to adjust horizontal grid size.
- **y_grid_size_slider** (`ipywidgets.IntSlider`): Slider to adjust vertical grid size.

#### Image Enhancement Controls

- **clahe_btn** (`ipywidgets.ToggleButton`): Toggle button to enable/disable CLAHE enhancement.
- **clahe_limit_slider** (`ipywidgets.FloatLogSlider`): Slider to adjust CLAHE limit.
- **subtract_background_btn** (`ipywidgets.ToggleButton`): Toggle button for background subtraction.
- **cmap_down** (`ipywidgets.Dropdown`): Dropdown to select the colormap.

#### Manual Annotation Controls

- **draw_mode_btns** (`ipywidgets.ToggleButtons`): Buttons to select drawing mode (Off/Add/Erase).
- **brush_size_slider** (`ipywidgets.FloatSlider`): Slider to adjust brush size.

#### Automatic Annotation Controls

- **annotate_btn** (`ipywidgets.Button`): Button to trigger automatic annotation.
- **hide_annotation_btn** (`ipywidgets.ToggleButton`): Toggle button to hide/show annotations.
- **threshold_slider** (`ipywidgets.FloatSlider`): Slider to adjust brightness threshold.
- **small_object_size** (`ipywidgets.FloatSlider`): Slider to adjust minimum object size.

### Data Access Properties

- **mask** (`numpy.ndarray`): The current annotation mask as a binary array.
- **canvas_widget** (`CanvasWidget`): The underlying canvas widget instance.
- **original_img** (`numpy.ndarray`): The original input image.

## Methods

### `get_metrics(brightness_mode='luminance-inverse')`

Calculates metrics for the annotated image based on the current grid.

#### Parameters

- **brightness_mode** (`str`, optional): Mode for brightness calculation. Default is 'luminance-inverse'.

#### Returns

- A dictionary containing the following metrics:
  - **integral_opacity**: Total opacity within each grid cell.
  - **average_opacity**: Average opacity per pixel in each grid cell.
  - **relative_area**: Proportion of each grid cell that is annotated.
  - **num_pixels**: Count of annotated pixels in each grid cell.

#### Example

```python
# Get metrics from the widget
metrics = widget.get_metrics()

# Access specific metrics
integral_opacity = metrics['integral_opacity']
average_opacity = metrics['average_opacity']
relative_area = metrics['relative_area']
num_pixels = metrics['num_pixels']
```

### `apply_auto_annotation(*args)`

Applies automatic annotation based on the threshold and size settings.

#### Parameters

- ***args**: Unused parameters to maintain compatibility with button callbacks.

#### Returns

- None

#### Example

```python
# Configure and run automatic annotation
widget.threshold_slider.value = 1.2
widget.small_object_size.value = 0.8
widget.apply_auto_annotation()
```

### `cut_img(img)`

Cuts the image according to the current grid padding.

#### Parameters

- **img** (`numpy.ndarray`): The image to cut.

#### Returns

- The cut image as a NumPy array.

### `_update_preprocessed_image(*args)`

Updates the preprocessed image based on current enhancement settings.

#### Parameters

- ***args**: Unused parameters to maintain compatibility with callbacks.

#### Returns

- None

## Events and Callbacks

The BactoWidget sets up numerous event handlers for its controls. The main ones are:

- The `clahe_btn`, `clahe_limit_slider`, and `subtract_background_btn` widgets are linked to the `_update_preprocessed_image` method.
- The `cmap_down` dropdown is linked to the `_update_image_view` method.
- The `draw_mode_btns` and `brush_size_slider` are linked to the Canvas widget.
- The `annotate_btn` is linked to the `apply_auto_annotation` method.
- The `hide_annotation_btn` is linked to the `_hide_annotation_clicked` method.
- The `change_grid_btn` is linked to the `_change_grid_btn_clicked` method.

## Usage Examples

### Basic Usage

```python
from bactovision.widget import BactoWidget
import matplotlib.pyplot as plt

# Create and display the widget
widget = BactoWidget('bacteria_image.png')
widget  # This displays the widget in the notebook

# After annotation, extract and visualize metrics
metrics = widget.get_metrics()
plt.figure(figsize=(10, 6))
plt.imshow(metrics['integral_opacity'])
plt.colorbar()
plt.title('Integral Opacity')
plt.show()
```

### Programmatic Control

```python
# Configure grid
widget.x_grid_size_slider.value = 10
widget.y_grid_size_slider.value = 8

# Enable image enhancements
widget.clahe_btn.value = True
widget.clahe_limit_slider.value = 200
widget.subtract_background_btn.value = True

# Set annotation parameters
widget.threshold_slider.value = 1.1
widget.small_object_size.value = 0.7

# Run auto-annotation
widget.apply_auto_annotation()
```

For more examples, see the [Examples](../examples.md) page.
