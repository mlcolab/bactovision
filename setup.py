"""Setup script for BactoVision package."""

from setuptools import find_packages, setup

setup(
    name="bactovision",
    version="0.1.0",
    description="A package for bacterial image processing",
    author="Vladimir Starostin",
    author_email="vladimir.starostin@uni-tuebingen.de",
    url="https://github.com/StarostinV/bactovision",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=[
        "numpy>=1.20.0,<2.0.0",
        "scipy>=1.8.0,<1.15.0",
        "scikit-image>=0.18.0,<0.20.0",
        "Pillow>=9.0.0,<10.0.0",
        "opencv-python>=4.5.0,<5.0.0",
        "anywidget>=0.1.0,<1.0.0",
        "traitlets>=5.0.0,<6.0.0",
        "matplotlib>=3.5.0,<4.0.0",
        "jupyterlab>=3.0.0,<4.0.0",
    ],
    python_requires=">=3.8,<3.11",
)
