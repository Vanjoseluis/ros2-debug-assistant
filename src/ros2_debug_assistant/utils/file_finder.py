from pathlib import Path

def find_python_files(root):
    return list(Path(root).rglob("*.py"))
