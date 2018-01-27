# Enter your code here. Read input from STDIN. Print output to STDOUT

"""Calculate the value of the Spearman's Rank correlation coefficient"""

n = raw_input()
X = raw_input()
Y = raw_input()

X,Y = X.split(" "), Y.split(" ")
X.pop()
X = [float(i) for i in X]
Y = [float(i) for i in Y]

rX = [sorted(X).index(i) + 1 for i in X]
rY = [sorted(Y).index(i) + 1 for i in Y]

print(round(1 - (6 * sum([(x - y) ** 2 for x, y in zip(rX, rY)])) / (float(n)**3 - float(n)), 3))
