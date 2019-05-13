#https://docs.python.org/3/library/itertools.html
import math
import cProfile

factorial=math.factorial
mem_choose = {}

def nCr(n, k):
    """
    N choose K
    """
    key = (n, k)
    if key not in mem_choose:
        if k > n:
            c = 0
        elif k==0 or n==k:
            c = 1
        elif k==1 or k==n-1:
            c = n
        else:
            c = factorial(n)//factorial(k)//factorial(n-k)
        mem_choose[key] = c
    return mem_choose[key]

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
return line

def listPascal(n):
    for i in range(1,n):
    print(pascal(i))

#cProfile.run("nCr(50000,44)")
print(nCr(500,499))
