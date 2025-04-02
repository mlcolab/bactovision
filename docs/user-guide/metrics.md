## Available Metrics

After annotating your image, you can get metrics for each grid cell using:

```python
metrics = widget.get_metrics()
```

This returns a dictionary with the following metrics:

- **integral_opacity** - Total opacity within each grid cell
- **average_opacity** - Average opacity per pixel in each grid cell
- **relative_area** - Proportion of each grid cell that is annotated
- **num_pixels** - Count of annotated pixels in each grid cell

Each metric is returned as a 2D NumPy array matching the grid dimensions.

### Visualizing Grid Metrics

You can visualize these metrics using matplotlib:

```python
import matplotlib.pyplot as plt

# Get metrics
metrics = widget.get_metrics()

# Visualize integral opacity
plt.figure(figsize=(10, 8))
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
