def arrayReplace(inputArray, elemToReplace, substitutionElem):
    """Replace all occurrences of elemToReplace with substitutionElem"""
    return [x if x != elemToReplace else substitutionElem for x in inputArray]
