# Installation Guide

BactoVision is designed to work within Jupyter notebooks and can be installed via pip. The package is compatible with Python 3.7+ and includes all necessary dependencies.

## Prerequisites

Before installing BactoVision, ensure you have Python 3.7 or higher.

## Installation Methods

### Standard Installation

The easiest way to install BactoVision is using pip:

```bash
pip install bactovision
```

This will install BactoVision along with all its dependencies.

### Installation from Source

For the latest development version or to contribute to the project, you can install from source:

```bash
git clone https://github.com/mlcolab/bactovision.git
cd bactovision
pip install .
```

## Dependencies

BactoVision has the following dependencies, which will be automatically installed with pip:

- numpy
- scipy
- scikit-image
- Pillow
- opencv-python
- anywidget
- traitlets
- matplotlib
- jupyterlab

## Verifying Installation

To verify that BactoVision is installed correctly, open a Jupyter notebook and run:

```python
from bactovision.widget import BactoWidget
print(BactoWidget)
```

If the installation was successful, this should print the widget class information without any errors.

## Troubleshooting

### Common Issues

#### Missing Dependencies

If you encounter errors about missing dependencies, try reinstalling with:

```bash
pip install bactovision --force-reinstall
```

#### JupyterLab Extension Issues

For JupyterLab users, if the widget doesn't display properly, ensure that the widget extension is installed:

```bash
jupyter labextension list
```

The output should include `anywidget` or similar entries. If not, you may need to run:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

### Getting Help

If you experience any issues with installation, please [open an issue](https://github.com/mlcolab/bactovision/issues) on our GitHub repository with details about the problem and your environment.
