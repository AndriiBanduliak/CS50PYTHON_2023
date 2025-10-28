# Python Practice Collection

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/username/python-practice/actions/workflows/tests.yml/badge.svg)](https://github.com/username/python-practice/actions/workflows/tests.yml)

A comprehensive collection of Python practice problems and solutions, covering various programming concepts from basic to intermediate level. This repository contains implementations of common algorithms, data structures, and practical utilities.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Available Scripts](#available-scripts)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Diverse Problem Set**: Covers string manipulation, data processing, API integration, and more
- **Clean Code**: Well-documented and following Python best practices
- **Test Coverage**: Comprehensive test suite for all modules
- **Modular Design**: Each script is self-contained and reusable
- **Error Handling**: Robust error handling and input validation

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/username/python-practice.git
cd python-practice
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

Each script can be run independently. Here are some examples:

```bash
# Bitcoin price calculator
python bitcoin/bitcoin.py 1.5

# ASCII art generator
python figlet/figlet.py -f slant "Hello World"

# Bank greeting analyzer
python bank/bank.py

# Cookie jar simulator
python jar/jar.py
```

## 📁 Project Structure

```
python-practice/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── lint.yml
├── adieu/              # Name list formatter
├── bank/               # Greeting analyzer
├── bitcoin/            # Bitcoin price calculator
├── camel/              # Camel case converter
├── coke/               # Coke machine simulator
├── deep/               # Deep question generator
├── einstein/           # Einstein's riddle solver
├── emojize/            # Emoji converter
├── extensions/         # File extension checker
├── faces/              # Face detection
├── figlet/             # ASCII art generator
├── fuel/               # Fuel gauge simulator
├── game/               # Number guessing game
├── grocery/            # Grocery list manager
├── indoor/             # Indoor temperature checker
├── interpreter/        # Python interpreter
├── jar/                # Cookie jar simulator
├── lines/              # Line counter
├── meal/               # Meal time formatter
├── numb3rs/            # IP address validator
├── nutrition/          # Nutrition facts
├── outdated/           # Date checker
├── pizza/              # Pizza calculator
├── plates/             # License plate validator
├── playback/           # Playback speed
├── professor/          # Grade calculator
├── response/           # Response generator
├── scourgify/          # Data cleaner
├── seasons/            # Season calculator
├── shirt/              # Shirt size calculator
├── shirtificate/       # Certificate generator
├── taqueria/           # Taco menu
├── tip/                # Tip calculator
├── twttr/              # Twitter text converter
├── um/                 # Word counter
├── watch/              # Watch time
└── working/            # Working hours calculator
```

## 🛠 Available Scripts

### Text Processing
- **adieu**: Formats name lists with proper grammar
- **camel**: Converts strings to camelCase
- **emojize**: Converts text to emojis
- **figlet**: Generates ASCII art text
- **playback**: Adjusts text playback speed
- **scourgify**: Cleans and formats data
- **twttr**: Removes vowels from text (Twitter-style)

### Data Validation
- **bank**: Analyzes greeting politeness
- **extensions**: Validates file extensions
- **numb3rs**: Validates IP addresses
- **plates**: Validates license plates
- **seasons**: Validates date formats

### Calculators & Utilities
- **bitcoin**: Bitcoin price calculator
- **fuel**: Fuel gauge simulator
- **meal**: Meal time formatter
- **nutrition**: Nutrition facts calculator
- **pizza**: Pizza size calculator
- **professor**: Grade calculator
- **tip**: Tip calculator
- **working**: Working hours calculator

### Games & Interactive
- **game**: Number guessing game
- **einstein**: Einstein's riddle solver
- **deep**: Deep question generator

### Data Processing
- **grocery**: Grocery list manager
- **jar**: Cookie jar simulator
- **lines**: Line counter
- **um**: Word counter

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest

# Run tests for specific module
python -m pytest jar/

# Run with coverage
python -m pytest --cov=.
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by CS50's Introduction to Computer Science
- Thanks to all contributors who have helped improve this project

---

⭐ If you found this project helpful, please give it a star!