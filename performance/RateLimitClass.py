#challenge notes
#took all 45 mins and ran out of time
#had a number of silly class mistakes/syntax errors
#misinterpreted the definition of 'rolling period'
#needed a number of hints

import time

def func():
    print('func')

class RateLimitPerSecond:
    '''
        Write a Rate Limit class that takes a function and limits it from being called more than once every n seconds
        func: function to be called
        seconds: some amount of time in s
    '''
    max_seconds = 10000

    def __init__(self, func, seconds=1):
        if seconds >=0 and seconds < RateLimitPerSecond.max_seconds:
            self.func = func
            self.seconds = seconds
            self.last_called = None
        else:
            print('seconds out of range')

    def apply(self):
        if not self.last_called:
            self.func()
            self.last_called = time.time()
        else:
            if (self.last_called + self.seconds) < time.time():
                self.func()
                self.last_called = time.time()
            else:
                print("called too soon")

def unit_test_per_second_good():
    print('unit_test_per_second_good')
    r = RateLimitPerSecond(func, 0)
    r.apply()
    time.sleep(.01)
    r.apply() # good because it happens immediately
    print("Good")
    
def unit_test_per_second_bad():
    print('unit_test_per_second_bad')
    r = RateLimitPerSecond(func, 1)
    r.apply()
    r.apply() # fails because it happens within 1s

class RateLimitPerCalls:
    '''
        Write a class that takes a function and limits it from being called more than once every n seconds
        func: function to be called
        max_calls: number of times func is allowed to be called in an n seconds period
    '''
    seconds_period = 1
    max_num_calls = 10000

    def __init__(self, func, max_calls):
        if max_calls >=0 and max_calls < RateLimitPerCalls.max_num_calls:
            self.func = func
            self.max_calls = max_calls
            self.func_called_list = []
        else:
            print('max_calls out of range')

    def apply(self):
        if self.max_calls == 0:
            print('called too many times”')
            return
        if not self.func_called_list:
            self.func()
            self.func_called_list.append(time.time())
        else:
            if (time.time() < (self.func_called_list[0] + RateLimitPerCalls.seconds_period)):
                if len(self.func_called_list) < self.max_calls:
                    self.func()
                    self.func_called_list.append(time.time())
                else:
                    print('called too many times”')
            else:
                self.func()
                self.func_called_list = [time.time()]
##        print(self.func_called_list)


def unit_test_per_calls_good():
    print('unit_test_per_calls_good')
    r = RateLimitPerCalls(func, 2)
    for i in range(2):
        r.apply() # 2 immediate calls is within the set max_calls
    print("Good")
    
def unit_test_per_calls_good2():
    print('unit_test_per_calls_good2')
    r = RateLimitPerCalls(func, 2)
    for i in range(2):
        r.apply() 
    time.sleep(1)
    r.apply() #after one second, the rolling window has passed and you can call again
    print("Good")

def unit_test_per_calls_bad():
    print('unit_test_per_calls_bad')
    r = RateLimitPerCalls(func, 0)
    for i in range(2):
        r.apply() # 2 immediate calls is within the set max_calls
    print("Good")
    
def unit_test_per_calls_bad2():
    print('unit_test_per_calls_bad2')
    r = RateLimitPerCalls(func, 2)
    for i in range(3):
        r.apply() # 2 ok, 1 time fail (assuming there are no more calls in the rolling 1s window)
    
def unit_test_per_calls_bad3():
    print('unit_test_per_calls_bad3')
    r = RateLimitPerCalls(func, 2)
    for i in range(2):
        r.apply() 
    time.sleep(.5)
    r.apply() # 2 ok, 1 time fail, only .5 seconds have passed


unit_test_per_second_good()
unit_test_per_second_bad()
unit_test_per_calls_good()
unit_test_per_calls_good2()
unit_test_per_calls_bad()
unit_test_per_calls_bad2()
unit_test_per_calls_bad3()

