# Enter your code here. Read input from STDIN. Print output to STDOUT

"""What is the probability that all 100 students will be able to purchase tickets?"""

import math

def cdf(std, mu, x):
    return 0.5 * (1 + math.erf((x-mu) / (std * math.sqrt(2))))

print round(cdf(math.sqrt(100) * 2.0, 100 * 2.4, 250), 4)
