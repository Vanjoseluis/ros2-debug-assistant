# Contributing to ros2-debug-assistant

Thank you for your interest in contributing to ros2-debug-assistant. This project aims to improve the ROS 2 development workflow by providing diagnostics and automated fixes for formatting, linters, dependencies, and common package issues.

Contributions of all kinds are welcome: bug reports, feature requests, documentation, tests, and code improvements.

## How to Contribute

### 1. Fork the repository

    git clone https://github.com/<your-username>/ros2-debug-assistant.git
    cd ros2-debug-assistant

### 2. Create a new branch

    git checkout -b my-feature-branch

### 3. Make your changes
Keep commits focused and meaningful. Follow the project’s coding style.

### 4. Run tests

    pytest

Add tests for any new functionality.

### 5. Submit a Pull Request
Open a PR against the main branch and describe:
- what you changed
- why the change is needed
- how it was tested

## Development Setup

Install dependencies:

    pip install -r requirements.txt

Install the package in editable mode:

    pip install -e .

Run the tool locally:

    ros2-debug-assistant check <path>

## Code Style

This project uses:
- PEP8 conventions
- Black for formatting
- isort for import ordering
- flake8 for linting

Run all formatters:

    black .
    isort .
    flake8

## Project Structure

    ros2-debug-assistant/
    │
    ├── src/ros2_debug_assistant/
    │   ├── cli.py
    │   ├── analyzer.py
    │   ├── fixer.py
    │   └── utils.py
    │
    ├── tests/
    │   └── test_basic.py
    │
    ├── README.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    └── requirements.txt

## Reporting Issues

When opening an issue, include:
- a clear description of the problem
- steps to reproduce
- expected vs. actual behavior
- environment details (OS, Python version, ROS 2 distro)

## Feature Requests

Describe:
- the problem the feature solves
- why it is useful
- how it might work

## Code of Conduct

Be respectful and constructive. This project follows the principles of the Contributor Covenant.

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
