import cProfile
from functools import reduce

def factors(n):
    '''
            Returns list of all divisors n 
    '''
    step = 2 if n%2 else 1       
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1, step) if n % i == 0)))  

def primeFactors(n):
    '''
            Returns list of primes that divide n 
    '''
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
    '''
            Generator of prime factors of n
    '''
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
        
def cnt_prime_Factors(n):
    '''
            Returns dictionary of (prime, count) pairs that divide n 
    '''
    fact = {}
    i=2
    while n % i == 0:
        n //= i
        if i in fact:
            fact[i]+=1
        else:
            fact[i]=1
    i=3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            if i in fact:
                fact[i]+=1
            else:
                fact[i]=1
    if n > 1:
        if n in fact:
            fact[n]+=1
        else:
            fact[n]=1
    return fact
	
#https://en.wikipedia.org/wiki/Divisor_function#Properties
def cnt_divisors(n):
    '''
            Returns the count of divisors of n, ex(28)=6 (1,2,4,7,14,28)
    '''
    cnt=1
    #cnt_primes=num_prime_Factors(n)
    for cnt_prime in cnt_prime_Factors(n).values():
         cnt*=(cnt_prime+1)
    return cnt
	
#n=100000000000000000000000000000000000000
#n=735734573573498646511235123
#print(len(str(n)))
#print(primeFactors(176400))
#print(list(primeFactorsGenerator(176400)))
#cProfile.run('print(primeFactors(n))')
#cProfile.run('print(primeFactorsGenerator(n))')
#cProfile(max(primeFactors(600851475143)))

