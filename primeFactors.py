import cProfile
from functools import reduce

def primeFactors(n):
    fact = []
    i=2
    while n % i == 0:
        n //= i
        fact.append(i)
    i=3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            fact.append(i)
    if n > 1:
        fact.append(n)
    return fact

def primeFactorsGenerator(n):   #about the same run time
    i=2
    while n % i == 0:
        n //= i
        yield i
    i=3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            yield i
    if n > 1:
        yield i

def factors(n):     
    step = 2 if n%2 else 1       
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1, step) if n % i == 0)))   
        
#n=100000000000000000000000000000000000000
#n=735734573573498646511235123
#print(len(str(n)))
#print(primeFactors(176400))
#print(list(primeFactorsGenerator(176400)))
#cProfile.run('print(primeFactors(n))')
#cProfile.run('print(primeFactorsGenerator(n))')
#cProfile(max(primeFactors(600851475143)))
