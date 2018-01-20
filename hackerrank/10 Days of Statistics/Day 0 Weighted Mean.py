# Enter your code here. Read input from STDIN. Print output to STDOUT

"""Compute weighted mean"""

n = raw_input()
integers = raw_input().split(" ")
weights = raw_input().split(" ")

numerator, denominator = 0, 0

for i in range(len(integers)):
    numerator += int(integers[i]) * int(weights[i])
    denominator += int(weights[i])

weighted_mean = numerator/float(denominator)
print round(weighted_mean, 1)
