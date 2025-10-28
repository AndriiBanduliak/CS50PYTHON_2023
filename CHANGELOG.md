# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- Comprehensive documentation
- GitHub Actions CI/CD workflows
- Code quality tools (Black, flake8, mypy)
- Pre-commit hooks configuration
- Issue and PR templates
- Security policy and code of conduct

### Changed
- Improved code structure and documentation
- Enhanced error handling in Bitcoin calculator
- Better user experience in Figlet ASCII art generator
- Improved greeting analysis logic in Bank module

### Fixed
- Fixed potential issues with input validation
- Improved error messages and user feedback

## [1.0.0] - 2024-01-01

### Added
- Bitcoin price calculator with CoinDesk API integration
- ASCII art generator using Figlet
- Bank greeting analyzer
- Cookie jar simulator
- IP address validator
- Season calculator
- Various utility scripts and tools

### Features
- **Bitcoin Calculator**: Real-time Bitcoin price calculation
- **ASCII Art Generator**: Text to ASCII art conversion with multiple fonts
- **Bank Greeting Analyzer**: Politeness-based tip calculation
- **Cookie Jar Simulator**: Interactive cookie jar management
- **IP Validator**: IPv4 address validation
- **Season Calculator**: Date-based season determination
- **Text Processing**: Various text manipulation utilities
- **Data Validation**: Input validation and sanitization tools

### Technical Details
- Python 3.8+ compatibility
- Comprehensive test coverage
- Type hints throughout codebase
- Modern Python packaging with pyproject.toml
- GitHub Actions for automated testing and deployment
- Pre-commit hooks for code quality
- Detailed documentation and examples

## [0.1.0] - 2023-12-01

### Added
- Initial collection of Python practice problems
- Basic script implementations
- Simple test cases

---

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):

- **MAJOR** version when you make incompatible API changes
- **MINOR** version when you add functionality in a backwards compatible manner
- **PATCH** version when you make backwards compatible bug fixes

## Release Process

1. Update version numbers in `pyproject.toml` and `setup.py`
2. Update this changelog
3. Create a git tag with the version number
4. Push changes and tags to the repository
5. GitHub Actions will automatically create a release

## Contributing

When contributing to this project, please:

1. Update the changelog for any user-facing changes
2. Follow the existing changelog format
3. Group changes by type (Added, Changed, Fixed, Removed, Security)
4. Use present tense ("Add feature" not "Added feature")
5. Reference issues and pull requests when applicable