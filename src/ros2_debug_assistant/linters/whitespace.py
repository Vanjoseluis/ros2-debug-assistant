def check_whitespace(lines):
    issues = []
    for i, line in enumerate(lines, start=1):
        if line.rstrip() != line:
            issues.append(f"Line {i}: trailing whitespace")
    return issues
