# Enter your code here. Read input from STDIN. Print output to STDOUT

"""What percentage of the students:
1. Scored higher than 80?
2. Passed the test?
3. Failed the test?"""

import math

#cumulative distribution function
def cdf(std, mu, x):
    return 0.5 * (1 + math.erf((x-mu) / (std * math.sqrt(2))))

#scored higher than 80
a1 = 1 - cdf(10, 70, 80)
print round(a1*100, 2)

#passed the test (>60)
a2 = 1 - cdf(10, 70, 60)
print round(a2*100, 2)

#failed the test (<60)
a3 = cdf(10, 70, 60)
print round(a3*100, 2)
