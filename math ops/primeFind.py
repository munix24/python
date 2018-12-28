import cProfile

def primes_sieve(limit):    #most efficient for limit < 10mil
    primes = [True] * (limit)
    primes[0] = primes[1] = False

    for i in range(2, limit):
        if primes[i]:         #only loop primes
            for n in range(i*i, limit, i):
                primes[n] = False
    return primes

def list_primes(limit):    #most efficient for limit < 10mil
    primes = primes_sieve(limit)
    listPrimes = [i for i in range(len(primes)) if primes[i]]
    return listPrimes

def nthPrime(n,limit):
    primes=primes_sieve(limit)
    if n<len(primes):
        return primes[n]
    return 0

def isPrime(val): # prime # always in the form 6k+-1
    if( val == 2 or val == 3 ):
        return True
    elif( val <= 1 or val%2 == 0  or val%3 == 0 ):
        return False
    for i in range( 5 , (round( val**.5 )+1) , 6 ):
        if( val%i == 0 or  val%(i+2) == 0  ):
            return False
    return True

def isPrime2(val): # Simple prime number test. Not as fast as isPrime
    if( val == 2 or val == 3 ):
        return True
    elif( val <= 1 or val%2 == 0 ):
        return False
    for i in range( 3 , (round( val**.5 )+1) , 2 ):
        if( val%i == 0 ):
            return False
    return True
	
def nthPrimenotSieve(n):
    count = 0
    i = 2
    while(count <= n):
        if isPrime(i):
            count += 1
        i += 1
    return i-1
	
n=1000001
#print(nthPrime(5,12))
#print(retPrimes(12))
#print(primes[10001-1])
#cProfile.run("nthPrime(100001,100000000)")
#cProfile.run("notSieve(n)")
