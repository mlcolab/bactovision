.PHONY: format lint test clean docs install-dev

# Format code
format:
	black bactovision tests
	python -m isort bactovision tests

# Lint code
lint:
	flake8 bactovision tests
	black --check bactovision tests
	python -m isort --check bactovision tests

# Run tests
test:
	pytest tests

# Run tests with coverage
test-cov:
	pytest --cov=bactovision tests

# Clean up build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Install in development mode
install-dev:
	pip install -e .
	pip install -r requirements-dev.txt
	pre-commit install

# Build documentation
docs:
	mkdocs build

# Serve documentation locally
docs-serve:
	mkdocs serve 