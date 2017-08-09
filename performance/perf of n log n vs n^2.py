import sys
import random
import cProfile

def meth1(S):
    #S=[x for x in range(10000000)]
    minn = 1000000000
    S = sorted(S)
    for s in range(1,len(S)):
        minn = min(minn, S[s]-S[s-1])
    print(minn)

def meth2(S):
    #S=[x for x in range(10000000)]
    minn = 1000000000
    for s in range(len(S)):
        for t in range(s+1, len(S)):
            minn = min(minn, abs(S[s]-S[t]))
    print(minn)

n = 10000
#S= random.sample(xrange(n*10000), n)
S= random.sample(xrange(n), n)
#meth1(S)
#cProfile.run('meth1(S)')
cProfile.run('meth2(S)')
