def edit_names(diff):
    if diff is False:
        diff = "false"
    if diff is True:
        diff = "true"
    if diff is None:
        diff = "null"
    return diff
