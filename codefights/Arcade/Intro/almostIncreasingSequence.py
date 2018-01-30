def almostIncreasingSequence(sequence):
    """determines whether it is possible to obtain a stricly increasing sequence by removing no more than one element from the array"""
    copy = sequence[:]
    for i in range(len(sequence) - 1):
        first, second = sequence[i], sequence[i+1]
        if first >= second:
            del sequence[i]
            del copy[i+1]
            break
    return (all(i < j for i,j in zip(sequence, sequence[1:])) or
            all(i < j for i,j in zip(copy, copy[1:])))
