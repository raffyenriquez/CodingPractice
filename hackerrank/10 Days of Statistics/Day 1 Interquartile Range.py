# Enter your code here. Read input from STDIN. Print output to STDOUT

""" calculate the interquartile range"""

n = raw_input()
array = raw_input()
freq = raw_input()
array = array.split(" ")
freq = freq.split(" ")

integers = []

for i in range(int(n)):
    for j in range(int(freq[i])):
        integers.append(int(array[i]))

integers = sorted(integers)

if len(integers) % 2 == 0:
    q1_list = integers[:(len(integers)/2)]
    q3_list = integers[(len(integers)/2):]

else:
    q1_list = integers[:int((len(integers)/2))]
    q3_list = integers[int((len(integers)/2))+1:]
    
def median(int_list):
    idx = len(int_list) / 2
    if len(int_list) % 2 != 0:
        return int_list[idx]
    return (int_list[idx] + int_list[idx-1]) / 2

#print iqr
print (float(median(q3_list)-median(q1_list)))
