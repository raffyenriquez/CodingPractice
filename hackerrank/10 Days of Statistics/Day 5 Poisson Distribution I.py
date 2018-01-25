# Enter your code here. Read input from STDIN. Print output to STDOUT

"""a random varaible, X, follows Poisson distribution tih mean of 2.5. Find the probability with which the random variable X is equal to 5."""

import math

def poisson(k, lam):
    return (lam**k * math.e**(-lam)) / math.factorial(k)

print round(poisson(5, 2.5), 3)
