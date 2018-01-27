# Enter your code here. Read input from STDIN. Print output to STDOUT

"""Calculate the value of the Pearson correlation coefficient"""

n = raw_input()
X = raw_input()
Y = raw_input()

X,Y = X.split(" "), Y.split(" ")
X.pop()
X = [float(i) for i in X]
Y = [float(i) for i in Y]

def mean(x):
    return sum(x) / float(len(x))

def std(x):
    return (sum((i - mean(x))**2 for i in x)/len(x))**(.5)

def pearson(X, Y):
    muX, muY = mean(X), mean(Y)
    stdX, stdY = std(X), std(Y)
    return sum([(X[i] - muX)*(Y[i] - muY) for i in range(len(X))]) / (len(X) * stdX * stdY)

print (round(pearson(X, Y), 3))
