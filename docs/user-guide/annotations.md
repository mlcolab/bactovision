# Annotations

This guide covers the annotation capabilities in BactoVision, which allow you to mark bacterial colonies and growth areas within your images.

## Annotation Methods

BactoVision offers two complementary annotation approaches:

1. **Automatic annotation** - Algorithm-based detection of bacterial colonies
2. **Manual annotation** - Direct drawing tools for fine-grained control

These approaches can be used individually or in combination to achieve the best results.

## Automatic Annotation

The automatic annotation feature uses thresholding techniques to identify bacterial colonies in your images.

### How It Works

The automatic annotation system works through the following steps:

1. Applies Otsu thresholding with a customizable threshold multiplier
2. Removes small objects below a specified size
3. Clears border objects
4. Creates convex hulls around the identified regions

### Configuring Automatic Annotation

You can adjust two key parameters to optimize automatic detection:

#### Brightness Threshold

The "Brightness threshold" slider controls the sensitivity of detection:

- **Higher values** (>1.0) - More restrictive detection, only selects very bright colonies
- **Lower values** (<1.0) - More inclusive detection, may include background noise

#### Smallest Size

The "Smallest size" slider determines the minimum size of colonies to be detected:

- **Higher values** - Ignores smaller colonies
- **Lower values** - Includes smaller colonies, but may include noise

### Running Automatic Annotation

To apply automatic annotation:

1. Adjust the threshold and size parameters
2. Click the "Apply auto" button

```python
# Programmatic control
widget.threshold_slider.value = 1.2  # Set brightness threshold
widget.small_object_size.value = 0.8  # Set smallest object size
widget.apply_auto_annotation()  # Run automatic annotation
```

## Manual Annotation

Manual annotation allows you to directly draw or erase annotations for precise control.

### Annotation Modes

The manual annotation system offers three modes:

- **Off** - Disables manual annotation
- **Add** - Enables drawing annotations
- **Erase** - Enables erasing annotations

### Brush Controls

The brush size can be adjusted using the slider:

- Larger brush sizes are useful for covering large areas quickly
- Smaller brush sizes provide fine-grained control for detailed work

### Using Manual Annotation

To manually annotate:

1. Select either "Add" or "Erase" mode
2. Adjust the brush size as needed
3. Click and drag on the canvas to draw or erase

```python
# Programmatic control
widget.draw_mode_btns.value = 'Add'  # Set to drawing mode
widget.brush_size_slider.value = 5   # Set brush size
```

## Combined Approach

For best results, consider using a combined approach:

1. Start with automatic annotation to quickly identify most colonies
2. Switch to manual annotation to:
   - Add missed colonies
   - Remove false positives
   - Refine boundaries

## Viewing and Hiding Annotations

You can toggle the visibility of annotations using the "Hide annotation" button. This is useful when you want to check the original image without annotations.

```python
# Hide annotations
widget.hide_annotation_btn.value = True

# Show annotations
widget.hide_annotation_btn.value = False
```

## Extracting Annotation Data

After annotation, you can extract the annotation mask:

```python
# Get binary mask of annotations
mask = widget.mask

# Analyze annotations per grid cell
metrics = widget.get_metrics()
```

## Advanced Techniques

### Fine-Tuning Image Before Annotation

For better annotation results, consider adjusting the image preprocessing:

1. Enable CLAHE to enhance contrast
2. Use background subtraction to remove uneven illumination
3. Experiment with different colormaps for better visibility

```python
# Enhance image for better annotation
widget.clahe_btn.value = True
widget.clahe_limit_slider.value = 200
widget.subtract_background_btn.value = True
widget.cmap_down.value = 'viridis'
```

### Handling Difficult Cases

For images with uneven backgrounds or complex growth patterns:

1. Start with a more permissive automatic threshold
2. Manually erase false positives
3. Add missed colonies by hand
4. Consider adjusting the grid to exclude problematic areas
