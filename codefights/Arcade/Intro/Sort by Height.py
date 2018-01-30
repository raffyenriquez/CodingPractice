def sortByHeight(a):
    """returns sorted heights without moving the trees between them"""
    heights = sorted([x for x in a if x != -1])
    index = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i] = heights[index]
            index += 1
    return a
