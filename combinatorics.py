#https://docs.python.org/3/library/itertools.html
import math
import cProfile

f=math.factorial

def nCr(n, k):
    return f(n)//f(k)//f(n-k)

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
