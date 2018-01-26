# Enter your code here. Read input from STDIN. Print output to STDOUT

"""A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, what is the probability tha all 49 boxes can be safely loaded into the freight elevator and transported?"""

import math

def cdf(std, mu, x):
    return 0.5 * (1 + math.erf((x-mu) / (std * math.sqrt(2))))

print round(cdf(math.sqrt(49) * 15, 49 * 205, 9800), 4)
