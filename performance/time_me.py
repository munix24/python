import time
import timeit

# @time_it
def test():
    L = [i for i in range(10000)]
    return L

# @time_it before function definition to call decorator 
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.6f} seconds to run.")
        return result
    return wrapper

def time_me(func, numbers = 1000, repeat = 3, *args):
    '''Not as precise for small operations due to other bg prc'''
    reps = []
    for r in range(repeat):
        start_t = time.time()
        for i in range(numbers):
            if args:
                func(args[0])
            else:
                func()
        reps.append(time.time()-start_t)
    print(reps)
    
##time_me(test)
##[0.8136627674102783, 0.563612699508667, 0.5866172313690186]

func = 'test'
setup = "from __main__ import " + func
number = 1000
repeat = 3
##print(timeit.timeit(func + '()', setup, timeit.default_timer, number))
##0.8164872723149565
print(timeit.repeat(func + '()', setup, timeit.default_timer, repeat, number))
##[0.8109674876421724, 0.9185773717445123, 1.1203567369395782]

