def alternatingSums(a):
    """returns an array of two integers each teh sum of alternating elements in an array"""
    return [sum(a[::2]), sum(a[1::2])]
