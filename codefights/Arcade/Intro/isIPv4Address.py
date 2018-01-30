def isIPv4Address(inputString):
    """given a string, find out if it satisfies the IPv4 address naming rules"""
    input = inputString.split(".")
    return len(input) == 4 and all(x.isdigit() and 0 <= int(x) <= 255 for x in input)
