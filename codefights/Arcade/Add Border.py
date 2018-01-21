def addBorder(picture):
    """adds a border around a matrix of characters"""
    
    with_border = []
    border = (len(picture[0]) + 2) * "*"
    
    with_border.append(border)
    
    for i in picture:
        with_border.append("*" + i + "*")
    
    with_border.append(border)
    
    return with_border
