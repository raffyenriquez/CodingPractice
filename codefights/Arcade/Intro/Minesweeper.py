def minesweeper(matrix):
    """creaete a Minesweeper game setup"""
    sweeped = []
    for i in range(len(matrix)):
        sweeped.append([]) 
        for j in range(len(matrix[0])):
            neighbors = -matrix[i][j]
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        neighbors += matrix[i+x][j+y]            
            sweeped[i].append(neighbors)
    return sweeped
