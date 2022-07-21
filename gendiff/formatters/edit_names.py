def edit_names(diff):
    if "False" in diff:
        diff = diff.replace("False", "false")
    if "True" in diff:
        diff = diff.replace("True", "true")
    if "None" in diff:
        diff = diff.replace("None", "null")
    return diff