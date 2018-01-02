#http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

#https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
		
@Memoize
def factorial(k):
    if k < 2: return 1
    return k * factorial(k - 1)

@Memoize
def factRecursion(n):        #NOT tail recursive 
    return 1 if n<=1 else n * factRecursion(n-1)

#print(factRecursion(100))

