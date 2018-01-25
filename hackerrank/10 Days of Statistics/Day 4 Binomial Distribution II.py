# Enter your code here. Read input from STDIN. Print output to STDOUT

"""a manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What us the probability that a batch of 10 pistons will contain:
1. No more than 2 rejects?
2. At least 2 rejects?"""

import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

#no more than 2 rejects
x, p, n = 0, .12/1, 10
for i in range(3):
    x += bi_dist(i, n, p)   
print round(x, 3)

#at least 2 rejects
x, p, n = 0, .12/1, 10
for i in range(2,11):
    x += bi_dist(i, n, p)   
print round(x, 3)
