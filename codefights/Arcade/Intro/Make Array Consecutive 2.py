def makeArrayConsecutive2(statues):
    """returns the number of statues needed to make a statue bigger than the previous statue by 1"""
    return max(statues) - min(statues) - len(statues) + 1
