import string

alphabet = string.ascii_lowercase + "a"

def alphabeticShift(inputString):
    """Given a string, replace each of its character by the next one in the English alphabet"""
    text = ""
    for i in inputString:
        if i.isalpha:
            index = alphabet.index(i)
            text += alphabet[int(index)+1]
        else:
            text += i
    return text
