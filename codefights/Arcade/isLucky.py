def isLucky(n):
    """determines if a given ticket number is lucky"""
    #number is considered lucky when sum of first half is equal to the sum of the second half
    l = len(str(n))
    n = map(int, str(n))
    return sum(n[:l/2]) == sum(n[l/2:l])

