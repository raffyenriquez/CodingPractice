def addBorder(picture):
    """adds a border around a matrix of characters"""
    l = (len(picture[0]) + 2)
    return ["*" * l] + ["*" + x + "*" for x in picture] + ["*" * l]
