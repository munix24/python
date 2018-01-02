import cProfile
import operator
import math

f=math.factorial

def factIter(n):
    num=1
    for i in range(2,n+1):
        num=num*i
    return num

def factIteration(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def factRecursion(n):        #NOT tail recursive
    return 1 if n<=1 else n * factRecursion(n-1)
	
def factLERecursion(n,m=1):  #NOT tail recursive
    if n<=1:
        return m
    else: 
        return factLERecursion(n-1,n*m)

#BEGIN TAIL RECURSION
#http://www.kylem.net/programming/tailcall.html
class TailCaller(object) :
    def __init__(self, f) :
        self.f = f
    def __call__(self, *args, **kwargs) :
        ret = self.f(*args, **kwargs)
        while type(ret) is TailCall :
            ret = ret.handle()
        return ret

class TailCall(object) :
    def __init__(self, call, *args, **kwargs) :
        self.call = call
        self.args = args
        self.kwargs = kwargs
    def handle(self) :
        if type(self.call) is TailCaller :
            return self.call.f(*self.args, **self.kwargs)
        else :
            return self.call(*self.args, **self.kwargs)

@TailCaller
def factTailRecursion(n, r=1) :
    if n <= 1 :
        return r
    else :
        return TailCall(factTailRecursion, n-1, n*r)

#cProfile.run('factTailRecursion(20000)')
print(factIter.__code__)

'''
run=factTailRecursion
param=20000
print(run(param))

if run.__module__ =='__main__':
    exec=run.__name__
else:
    exec=run.__module__+'.'+run.__name__
exec=exec+'('+str(param)+')'
cProfile.run(exec)
input()
'''
