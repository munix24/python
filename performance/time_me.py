import time
import timeit

def test():
    L = [i for i in range(10000)]
    return L

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

