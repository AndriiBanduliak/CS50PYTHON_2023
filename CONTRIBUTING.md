# Contributing to Python Practice Collection

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

Before creating an issue, please:
1. Check if the issue already exists
2. Use the issue templates provided
3. Provide clear steps to reproduce the problem
4. Include relevant system information

### Suggesting Enhancements

We welcome suggestions for new features or improvements. Please:
1. Check existing issues and discussions
2. Provide a clear description of the enhancement
3. Explain why it would be valuable
4. Consider implementation complexity

## 🚀 Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/python-practice.git
   cd python-practice
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Code Style Guidelines

### Python Style

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length**: 88 characters (Black formatter default)
- **Import order**: Standard library, third-party, local imports
- **Docstrings**: Use Google style docstrings
- **Type hints**: Use type hints for function parameters and return values

### Code Formatting

We use [Black](https://github.com/psf/black) for code formatting:

```bash
# Format all Python files
black .

# Check formatting without making changes
black --check .
```

### Linting

We use [flake8](https://flake8.pycqa.org/) for linting:

```bash
# Run linting
flake8 .

# Run with specific configuration
flake8 --max-line-length=88 --extend-ignore=E203,W503 .
```

### Type Checking

We use [mypy](https://mypy.readthedocs.io/) for static type checking:

```bash
# Run type checking
mypy .
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=.

# Run specific test file
python -m pytest tests/test_specific_module.py

# Run tests in verbose mode
python -m pytest -v
```

### Writing Tests

- Write tests for all new functionality
- Aim for high test coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Test both success and failure cases

### Test Structure

```python
def test_function_name_should_do_something_when_condition():
    """Test that function_name does something when condition is met."""
    # Arrange
    input_data = "test input"
    expected_output = "expected result"
    
    # Act
    result = function_name(input_data)
    
    # Assert
    assert result == expected_output
```

## 📋 Pull Request Process

1. **Update documentation** for any new features or changes
2. **Add tests** for new functionality
3. **Ensure all tests pass**:
   ```bash
   python -m pytest
   ```
4. **Run code formatting**:
   ```bash
   black .
   ```
5. **Run linting**:
   ```bash
   flake8 .
   ```
6. **Commit your changes** with a clear commit message
7. **Push to your fork** and create a Pull Request

### Commit Message Format

Use clear, descriptive commit messages:

```
feat: add new bitcoin price calculator
fix: resolve issue with jar withdrawal validation
docs: update README with installation instructions
test: add unit tests for figlet module
refactor: improve error handling in bank module
```

### Pull Request Template

When creating a PR, please include:

- **Description**: What changes were made and why
- **Type**: Bug fix, feature, documentation, etc.
- **Testing**: How the changes were tested
- **Breaking Changes**: Any breaking changes (if applicable)
- **Screenshots**: For UI changes (if applicable)

## 🏷️ Issue Labels

We use the following labels to categorize issues:

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements or additions to documentation
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed
- `question`: Further information is requested

## 📚 Documentation

### Code Documentation

- Use docstrings for all functions, classes, and modules
- Follow Google style docstrings
- Include type hints
- Provide examples for complex functions

### README Updates

- Update the main README.md for significant changes
- Add new scripts to the project structure
- Update usage examples
- Keep the table of contents current

## 🎯 Areas for Contribution

We especially welcome contributions in these areas:

- **New Scripts**: Add new practice problems
- **Test Coverage**: Improve test coverage
- **Documentation**: Improve code documentation
- **Performance**: Optimize existing code
- **Error Handling**: Improve error handling and validation
- **Code Quality**: Refactor and improve code structure

## ❓ Questions?

If you have questions about contributing:

1. Check existing issues and discussions
2. Create a new issue with the `question` label
3. Join our community discussions

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to Python Practice Collection! 🎉