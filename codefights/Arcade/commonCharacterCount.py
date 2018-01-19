def commonCharacterCount(s1, s2):
    """returns number of common characters between two strings"""
    common = 0
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                s2 = s2.replace(char2, "", 1)
                common += 1
                break
    return common
