.PHONY: help install install-dev test lint format clean build publish docs

# Default target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install -e ".[dev]"
	pre-commit install

test: ## Run tests
	python -m pytest -v --cov=. --cov-report=html --cov-report=term-missing

test-fast: ## Run tests without coverage
	python -m pytest -v

lint: ## Run linting
	flake8 .
	mypy . --ignore-missing-imports

format: ## Format code
	black .
	isort .

format-check: ## Check code formatting
	black --check .
	isort --check-only .

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	python -m build

publish: ## Publish to PyPI
	python -m build
	python -m twine upload dist/*

docs: ## Generate documentation
	@echo "Documentation is available in README.md"

security: ## Run security checks
	pip install safety
	safety check

pre-commit: ## Run pre-commit hooks
	pre-commit run --all-files

docker-build: ## Build Docker image
	docker build -t python-practice .

docker-run: ## Run Docker container
	docker run --rm -it python-practice

docker-test: ## Run tests in Docker
	docker run --rm python-practice python -m pytest -v

# Development workflow
dev-setup: install-dev ## Set up development environment
	@echo "Development environment set up successfully!"
	@echo "Run 'make test' to run tests"
	@echo "Run 'make lint' to check code quality"
	@echo "Run 'make format' to format code"

ci: lint test ## Run CI pipeline locally
	@echo "CI pipeline completed successfully!"

# Quick development commands
quick-test: ## Quick test run
	python -m pytest -xvs

quick-lint: ## Quick lint check
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Release commands
version-patch: ## Bump patch version
	bump2version patch

version-minor: ## Bump minor version
	bump2version minor

version-major: ## Bump major version
	bump2version major

release: clean build ## Create a release
	@echo "Creating release..."
	git tag -a v$(shell python -c "import setup; print(setup.version)") -m "Release v$(shell python -c "import setup; print(setup.version)")"
	git push origin --tags