# Enter your code here. Read input from STDIN. Print output to STDOUT

"""given a ration of boys to girls for babies born in Russia is 1.09 : 1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?"""

import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

x, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    x += bi_dist(i, n, p)   
print round(x, 3)
