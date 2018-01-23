# Enter your code here. Read input from STDIN. Print output to STDOUT

"""Compute mean, median and mode"""

n = raw_input()
array = raw_input()
integers = [int(i) for i in array.split(" ")]
    
#mean
print sum(integers) / float(n)

#median
sorted_integers = sorted(integers)
middle = [sorted_integers[int(n)/2], sorted_integers[int(n)/2 -1]]
print sum(middle) / 2.0

#mode
integer, freq = 0, 0
for i in sorted_integers:
    count = sorted_integers.count(i)
    if count > freq:
        integer = i
        freq = count
print integer

