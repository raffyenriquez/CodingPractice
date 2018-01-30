def commonCharacterCount(s1, s2):
    """returns number of common characters between two strings"""
    return sum(min(s1.count(x),s2.count(x)) for x in set(s1)) 
