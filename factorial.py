#https://www.codechef.com/problems/FCTRL2
import cProfile
import operator
import math

f=math.factorial

def factIter(n):
    return reduce(operator.mul,range(1,n+1),1)

def factIteration(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def factRecursion(n):         #NOT tail recursive
    return 1 if n<=1 else n * factRecursion(n-1)

def factLERecursion(n,prod):  #NOT tail recursive
    if n<=1:
        return prod
    else: 
        prod=(n-1)*prod
        return factLERecursion(n-1,prod)

def factLBRecursion(n,i=1,prod=1):  #NOT tail recursive
    if n<i:
        return prod
    else: 
        prod=i*prod
        return factLBRecursion(n,i+1,prod)

#cProfile.run("factIteration(100000)")
print(factIteration(5))