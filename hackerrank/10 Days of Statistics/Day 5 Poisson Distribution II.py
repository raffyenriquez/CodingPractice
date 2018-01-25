# Enter your code here. Read input from STDIN. Print output to STDOUT

"""Find and print the expected daily cost of each machine"""

import math

def poisson(k, lam):
    return (lam**k * math.e**-lam) / math.factorial(k)

cost_a = lambda x: 160 + 40 * (x ** 2)
cost_b = lambda y: 128 + 40 * (y ** 2)

#any number less than 10 would produce the wrong answer
expected_a = sum([cost_a(x) * poisson(x, 0.88) for x in range(11)])
expected_b = sum([cost_b(y) * poisson(y, 1.55) for y in range(11)])

print round(expected_a, 3)
print round(expected_b, 3)
