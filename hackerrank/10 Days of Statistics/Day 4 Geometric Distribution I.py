# Enter your code here. Read input from STDIN. Print output to STDOUT


"""the probability that a machine produces a defective product is 1/3. What is the probability that the 1st defecct is found during the 5th inspection?"""

def geo_dist(n,p):
    return ((1-p)**(n-1))*p

print round(geo_dist(5, 1/3.0), 3)
