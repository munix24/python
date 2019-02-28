import cProfile

def primes_sieve(limit):    #most efficient for limit<10mil
    primeList=[]
    primes = [True] * (limit)
    primes[0] = primes[1] = False
    i=2

    while(i<limit):
        if primes[i]:         #return prime and only loop primes
            for n in range(i*i, limit, i):
                primes[n] = False
        i=i+1
    return primes

def rotate_list(l, n):
    return l[n:] + l[:n]

def rotate_int(N):
    '''rotate digits in N. Different from permutation because order is preserved'''
    L = list(str(N))
    l = len(L)
    for a in range(l):
        yield int(''.join(rotate_list(L, a)))

def rotation_test(N):
    '''rotate digits and return true if all rotations are prime numbers'''
    ret = True
    for rot in rotate_int(N):
##        print(rot)
        if not primes[rot]:
            ret = False
    return ret

def main(N):
    rotations = []
    for i in range(2, N + 1):
        if primes[i]:   # test if i is prime
            if rotation_test(i):    # test if all rotations are prime
##                print(i)
                rotations.append(i)
##    print(len(rotations))
##    print(rotations)
    return sum(rotations)
    
n=1000001
N=int(input())

primes=primes_sieve(n)
print(main(N))


##print(rotation_test(197))
