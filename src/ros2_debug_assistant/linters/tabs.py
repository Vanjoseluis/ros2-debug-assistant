def check_tabs(lines):
    issues = []
    for i, line in enumerate(lines, start=1):
        if "\t" in line:
            issues.append(f"Line {i}: contains tab characters")
    return issues
