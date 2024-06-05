def split_nice(text: str,
               limit: int,
               first_string_limit: int = 0):
    split_text = []
    tmp_limit = 0
    while len(text) > limit:
        if first_string_limit:
            tmp_limit = limit
            limit = first_string_limit
        tmp = text[:limit]
        tmp = tmp[:tmp.rfind("\n")]
        split_text.append(tmp)
        text = text[len(tmp):]
        if first_string_limit:
            limit = tmp_limit
            first_string_limit = 0
    if len(text) > 0:
        split_text.append(text)
    return split_text
