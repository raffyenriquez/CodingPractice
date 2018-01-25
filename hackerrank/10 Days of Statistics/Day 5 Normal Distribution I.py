# Enter your code here. Read input from STDIN. Print output to STDOUT

"""In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:
1. Less than 19.5 hours?
2. Between 20 and 22 hours?"""

import math

#cumulative distribution function
def cdf(std, mu, x):
    return 0.5 * (1 + math.erf((x-mu) / (std * math.sqrt(2))))

#less than 19.5 hours
print round(cdf(2, 20, 19.5), 3)

#between 20 and 22 hours
print round(cdf(2, 20, 22) - cdf(2, 20, 20), 3)
