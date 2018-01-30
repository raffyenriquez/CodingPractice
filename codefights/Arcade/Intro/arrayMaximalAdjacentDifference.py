def arrayMaximalAdjacentDifference(inputArray):
    """given an array of integers, find the maximal absolute difference between any two of its adjacent elemtns"""
    return max([abs(x-y) for x, y in zip(inputArray, inputArray[1:])])
