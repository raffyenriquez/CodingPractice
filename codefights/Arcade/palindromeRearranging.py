def palindromeRearranging(inputString):
    """returns if a given string can be rearranged to form a palindrome"""
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1
