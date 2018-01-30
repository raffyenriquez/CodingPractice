def checkPalindrome(inputString):
    """checks if string is a plandrome"""
    #a palindrome is a word that reads the same forward and backward
    return inputString == inputString[::-1]
