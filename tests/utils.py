"""Utility functions for testing."""

import io

import numpy as np
from PIL import Image


def create_test_binary_mask(size=(50, 50)):
    """Create a test binary mask with some regions."""
    mask = np.zeros(size, dtype=bool)

    # Add a few regions
    mask[10:20, 10:20] = True
    mask[30:40, 30:40] = True

    return mask


def create_test_labeled_mask(size=(50, 50)):
    """Create a test labeled mask with some regions."""
    mask = np.zeros(size, dtype=np.int32)

    # Add a few regions
    mask[10:20, 10:20] = 1
    mask[30:40, 30:40] = 2

    return mask


def create_test_grayscale_image(size=(100, 100)):
    """Create a simple grayscale test image with some bright spots."""
    img = np.zeros(size, dtype=np.uint8)

    # Add a gradient background
    x, y = np.meshgrid(np.linspace(0, 50, size[1]), np.linspace(0, 50, size[0]))
    img += np.clip(x + y, 0, 50).astype(np.uint8)

    # Add a few bright spots
    img[20:30, 20:30] = 200
    img[60:80, 60:80] = 150

    return img


def create_test_color_image(size=(100, 100)):
    """Create a simple color test image with some bright spots."""
    img = np.zeros((size[0], size[1], 3), dtype=np.uint8)

    # Add a gradient background
    x, y = np.meshgrid(np.linspace(0, 50, size[1]), np.linspace(0, 50, size[0]))
    background = np.clip(x + y, 0, 50).astype(np.uint8)
    img[:, :, 0] = background
    img[:, :, 1] = background
    img[:, :, 2] = background

    # Add red spots
    img[20:30, 20:30, 0] = 200

    # Add green spots
    img[40:50, 40:50, 1] = 200

    # Add blue spots
    img[60:70, 60:70, 2] = 200

    # Add white spots
    img[80:90, 80:90] = 200

    return img


def image_to_bytes(img):
    """Convert a numpy array to bytes."""
    if isinstance(img, np.ndarray):
        # Convert numpy array to PIL Image
        if img.ndim == 2 or (img.ndim == 3 and img.shape[2] == 1):
            pil_img = Image.fromarray(img.squeeze(), mode="L")
        elif img.ndim == 3 and img.shape[2] == 3:
            pil_img = Image.fromarray(img, mode="RGB")
        else:
            raise ValueError(f"Unsupported image shape: {img.shape}")
    else:
        pil_img = img

    # Convert PIL Image to bytes
    img_bytes = io.BytesIO()
    pil_img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return img_bytes.getvalue()
