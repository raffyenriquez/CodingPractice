# Enter your code here. Read input from STDIN. Print output to STDOUT

"""the probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect is found during the first 5 inspection?"""

def geo_dist(n,p):
    return ((1-p)**(n-1))*p

print round(sum([geo_dist(i, 1/3.0) for i in range(1,6)]), 3)
