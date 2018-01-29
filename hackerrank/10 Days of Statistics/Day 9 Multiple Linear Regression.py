# Enter your code here. Read input from STDIN. Print output to STDOUT

"""Find the value of Y for each q feature sets."""

from sklearn import linear_model

m, n = raw_input().split(" ")
inputs = []
for i in range(int(n)):
    inputs.append([float(x) for x in raw_input().split(" ")])
y = [y.pop() for y in inputs]

lm = linear_model.LinearRegression()
lm.fit(inputs, y)
a = lm.intercept_
b = lm.coef_

q = raw_input()
fs = []
for i in range(int(q)):
    fs.append([float(x) for x in raw_input().split(" ")])

for i in range(int(q)):
    Y = 0
    for x in range(int(m)):
        Y += fs[i][x]*b[x]
    print a+Y
