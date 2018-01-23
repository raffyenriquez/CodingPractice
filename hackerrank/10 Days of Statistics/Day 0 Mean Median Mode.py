# Enter your code here. Read input from STDIN. Print output to STDOUT

"""compute mean, median and mode"""

n = raw_input()
array = raw_input()
integers = []

for i in array.split(" "):
    integers.append(int(i))
    
#mean
mean = sum(integers) / float(n)
print mean

#median
sorted_integers = sorted(integers)
middle = [sorted_integers[int(n)/2], sorted_integers[int(n)/2 -1]]
median = sum(middle) / 2.0
print median

#mode
integer, freq = 0, 0
for i in sorted_integers:
    count = sorted_integers.count(i)
    if count > freq:
        integer = i
        freq = count
mode = integer
print mode
