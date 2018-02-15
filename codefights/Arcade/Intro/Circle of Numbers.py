def circleOfNumbers(n, firstNumber):
    """Returns the radially opposite position of first number"""
    return (n/2 + firstNumber) % n
