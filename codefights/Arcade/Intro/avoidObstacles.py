def avoidObstacles(inputArray):
    """find the minimal length of the jump enough to avoid all the obstacles"""
    for i in range(1, max(inputArray)):
        if not any([x for x in inputArray if not x%i]):
            return i
    return max(inputArray) + 1
