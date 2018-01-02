import cProfile

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibm(n):
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#cProfile.run("fibm(1000)")
print(fibm(5))
