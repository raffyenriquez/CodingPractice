def matrixElementsSum(matrix):
    """returns total price of rooms suitable for bots to live in"""
    total = 0
    for elem in range(len(matrix[0])):
        for m in range(len(matrix)):
            if matrix[m][elem] == 0:
                break
            total += matrix[m][elem]
    return total
