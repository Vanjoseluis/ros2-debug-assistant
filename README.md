# ros2-debug-assistant

A **ROS 2 development assistant** that detects formatting issues, linter errors, missing dependencies and common pitfalls — and suggests or applies fixes automatically.  
Its goal is to reduce friction when developing or contributing to ROS 2 packages by providing clear diagnostics and actionable corrections.

---

## 🚀 Overview

Working with ROS 2 often involves dealing with linters, build tools, CMake, package manifests, and formatting conventions before your code even runs. Traditional debuggers (gdb, lldb, pdb) help inspect program logic, but they cannot detect:

- indentation errors  
- mixed tabs and spaces  
- missing dependencies in `package.xml`  
- incorrect CMake configuration  
- failing ament linters  
- inconsistent formatting  
- launch/test misconfigurations  

**ros2-debug-assistant** focuses on the *ecosystem* around your code, not the code execution itself. It analyzes your package structure, formatting, linters, and metadata to help you fix issues early and efficiently.

---

## ✨ Features (MVP)

- Detect trailing whitespace  
- Detect mixed tabs/spaces  
- Detect indentation inconsistencies  
- Detect overly long lines  
- Provide clear, human-readable diagnostics  
- Offer automatic fixes:
  - remove trailing whitespace  
  - convert tabs to spaces  
  - normalize indentation  
- Interactive mode:

```text
Fix indentation error on line 87?
[Y]es / [n]o / [s]kip / [S]kip all
```

Future versions will expand into dependency analysis, linter integration, test/launch validation, and editor integration.

---

## 📦 Installation

*(To be updated once the package is published.)*

For now, clone the repository:

```bash
git clone https://github.com/Vanjoseluis/ros2-debug-assistant
cd ros2-debug-assistant
pip install -r requirements.txt
```

---

## 🧪 Usage

Check a package or directory:

    ros2-debug-assistant check src/my_package

Apply automatic fixes:

    ros2-debug-assistant fix src/my_package

Interactive mode:

    ros2-debug-assistant interactive src/my_package

## 🧱 Architecture

    ros2-debug-assistant
    │
    ├── cli.py          # Command-line interface
    ├── analyzer.py     # Static analysis of files and package structure
    ├── fixer.py        # Automatic corrections and formatting fixes
    └── utils.py        # Shared helpers

The tool is designed to be modular so new analyzers and fixers can be added easily.

## 🗺️ Roadmap

### v0.1.0 — MVP
- Basic formatting analysis
- Basic automatic fixes
- CLI with check/fix/interactive modes
- Unit tests for core functionality

### v0.2.0 — Linter integration
- Parse ament_lint output
- Provide explanations for common linter errors
- Suggest fixes

### v0.3.0 — Dependency & CMake analysis
- Detect missing dependencies
- Detect unused dependencies
- Validate CMakeLists.txt structure

### v0.4.0 — Test & launch diagnostics
- Detect common pytest/launch_testing issues
- Validate launch files

### v0.5.0 — Editor integration
- VSCode extension
- “Accept fix” UI
- Real-time diagnostics
