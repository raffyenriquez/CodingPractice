# Enter your code here. Read input from STDIN. Print output to STDOUT

""" calculate the first quartile (q1), second quartile (q2), and third quartile (q3)"""

n = raw_input()
array = raw_input()
integers = sorted([int(i) for i in array.split(" ")])

if len(integers) % 2 == 0:
    q1_list = integers[:int(n)/2]
    q3_list = integers[int(n)/2:]
    
else:
    q1_list = integers[:int(n)/2]
    q3_list = integers[int(n)/2+1:]
    
def median(int_list):
    idx = len(int_list) / 2
    if len(int_list) % 2 != 0:
        return int_list[idx]
    return (int_list[idx] + int_list[idx-1]) / 2

#print q1, q2, q3
print median(q1_list)
print median(integers)
print median(q3_list)
