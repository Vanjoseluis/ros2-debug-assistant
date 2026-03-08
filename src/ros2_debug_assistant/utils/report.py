def format_report(issues):
    if not issues:
        return "No issues found."

    return "\n".join(issues)
