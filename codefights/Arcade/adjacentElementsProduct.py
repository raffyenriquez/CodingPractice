def adjacentElementsProduct(inputArray):
    """returns the product of the pair of adjacent elements with the largest product"""
    return max(x*y for x,y in zip(inputArray, inputArray[1:]))
