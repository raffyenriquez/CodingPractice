def arrayChange(inputArray):
    """returns minimal number of moves to obtain a strictly increasing sequence from input"""
    moves = 0
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            diff = inputArray[i] - inputArray[i+1] + 1
            inputArray[i+1] += diff
            moves += diff  
    return moves
