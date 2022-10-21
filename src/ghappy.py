def ghappy(string):
    assert string is not None
    for i in range(0, len(string)):
        if string[i] == "g":
            if i > 0 and string[i-1] == "g":
                continue
            if i + 1 < len(string) and string[i+1] == "g":
                continue
            return False

    return True
