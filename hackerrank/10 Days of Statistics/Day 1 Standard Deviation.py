# Enter your code here. Read input from STDIN. Print output to STDOUT

"""print the standard deviation"""

n = float(raw_input())
array = raw_input()
integers = sorted([int(i) for i in array.split(" ")])
    
#mean
mean = sum(integers) / n

var = sum((i - mean)**2 for i in integers)

#standard deviation
print round((var/n)**(.5), 1)
