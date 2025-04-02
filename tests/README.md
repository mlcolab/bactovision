# BactoVision Tests

This directory contains tests for the BactoVision package.

## Running Tests

You can run the tests with pytest:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=bactovision

# Run tests for a specific module
pytest tests/test_image_processing.py
```

## Test Structure

- `test_image_processing.py`: Tests for the image processing functions
- `utils.py`: Utility functions for creating test images and masks

## Writing New Tests

When adding new tests, follow these guidelines:

1. Use the utility functions in `utils.py` to create test images and masks
2. Test one function per test function
3. Name test functions with the prefix `test_`
4. Add docstrings to explain what the test is checking
5. Use assertions to verify expected behavior

## Test Dependencies

The tests require pytest and pytest-cov, which can be installed from the requirements-dev.txt file:

```bash
pip install -r requirements-dev.txt
``` 