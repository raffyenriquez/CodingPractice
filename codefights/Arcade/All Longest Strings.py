def allLongestStrings(inputArray):
    """returns an array of strings that contains all the longest strings"""
    longest = max([len(x) for x in inputArray])
    ls = []
    for i in inputArray:
        if len(i) == longest:
            ls.append(i)
    return ls
