def areSimilar(a, b):
    """return if two arrays are similar"""
    #similar if can be obtained by swapping at most one pair of elements in an array
    return sorted(a)==sorted(b) and sum([x!=y for x,y in zip(a,b)])<=2
