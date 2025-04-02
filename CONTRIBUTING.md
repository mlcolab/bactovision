# Contributing to BactoVision

Thank you for considering contributing to BactoVision! This document outlines the process for contributing to the project.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/StarostinV/bactovision.git
   cd bactovision
   ```

2. Set up the development environment (this installs all dependencies and pre-commit hooks):
   ```bash
   ./setup_dev.sh
   ```

   Alternatively, you can run these commands manually:
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   pre-commit install
   ```

## Development Workflow

We use pre-commit hooks to enforce code style and quality. These will run automatically when you commit your changes.

You can also run them manually:

```bash
# Format code
make format

# Lint code
make lint

# Run tests
make test

# Run tests with coverage
make test-cov
```

## Pull Request Process

1. Create a new branch for your feature or bugfix.
2. Make your changes, including appropriate test cases.
3. Run the tests and linters to ensure your code meets the project's standards.
4. Submit a pull request.

## Code Standards

We follow these coding standards:

1. **Style Guide**: We use Black for code formatting and isort for import sorting.
2. **Documentation**: All functions, classes, and modules should have docstrings.
3. **Testing**: All new features should be accompanied by tests.
4. **Type Hints**: Use type hints for function arguments and return values when feasible.

## Testing

We use pytest for testing. Make sure to run the tests before submitting a pull request:

```bash
pytest
```

You can also run tests with coverage:

```bash
pytest --cov=bactovision
```

## Documentation

We use MkDocs for documentation. To build the documentation locally:

```bash
mkdocs build
```

To serve the documentation locally:

```bash
mkdocs serve
```
