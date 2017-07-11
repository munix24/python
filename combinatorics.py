#https://docs.python.org/3/library/itertools.html
import math
import cProfile

f=math.factorial

def nCr(n, k):
    return f(n)//f(k)//f(n-k)

#cProfile.run("nCr(50000,44)")
print(nCr(500,499))
