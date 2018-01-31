def boxBlur(image):
    """return the blurred image as an integer using the box blur algorithm"""
    width = len(image[0])
    height = len(image)
    blurred = []
    for i in range(1, height-1):
        temp = []
        for j in range(1, width-1):
            total = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    total += image[x][y]
            temp.append(total/9)
        blurred.append(temp)
    return blurred
