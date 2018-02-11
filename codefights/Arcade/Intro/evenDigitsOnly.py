def evenDigitsOnly(n):
    """Check if all digits of the given integer are even"""
    return all([int(x) % 2 ==0 for x in str(n)])
