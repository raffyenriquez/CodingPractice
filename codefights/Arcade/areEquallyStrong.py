def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    """find out if two are equally strong"""
    return sorted([yourLeft, yourRight]) == sorted([friendsLeft, friendsRight])
