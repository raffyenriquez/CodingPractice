# Enter your code here. Read input from STDIN. Print output to STDOUT

"""Compute and print the value of y when x = 80"""

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

def mean(x):
    return sum(x) / float(len(x))

def std(x):
    return (sum((i - mean(x))**2 for i in x)/len(x))**(.5)

def pearson(X, Y):
    muX, muY = mean(X), mean(Y)
    stdX, stdY = std(X), std(Y)
    return sum([(X[i] - muX)*(Y[i] - muY) for i in range(len(X))]) / (len(X) * stdX * stdY)

muX = mean(X)
muY = mean(Y)
b = pearson(X, Y) * std(Y) / std(X)
a = muY - (b * muX)

#value of y given x = 80
print round(a + b * 80, 3)
