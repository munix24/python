import random
import cProfile

#.183s fastest
def gen_rand_bits():
    for _ in range(1000000):
        rand=random.getrandbits(1)

#1.530s calls on getrandbits and other methods
def gen_rand_ints():
    for _ in range(1000000):
        rand=random.randint(0, 1)

#3.253s calls a number of other methods
def gen_rand_sample():
    for _ in range(1000000):
        rand=random.sample([0, 1], 1)

cProfile.run('gen_rand_ints()')
cProfile.run('gen_rand_bits()')
cProfile.run('gen_rand_sample()')
