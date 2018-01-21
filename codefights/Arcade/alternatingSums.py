def alternatingSums(a):
    """returns an array of two integers each the sum of alternating elements in an array"""
    t1 = sum(a[::2])
    t2 = sum(a[1::2])
    return [t1, t2]
