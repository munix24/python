import itertools
import math
mem = {}

#itertools.permutations code
#https://docs.python.org/2/library/itertools.html#itertools.permutations

def perm(lst, r):
    return itertools.permutations(lst, r)
    
def permute(lst):
    """
    recursively generate sorted list of all possible permutations of lst
    permute([2,3]): choose 2, insert 2 before permute([3]), yield [2,3]
    permute([2,3]): choose 3, insert 3 before permute([2]), yield [3,2]
    permute([1,2,3]): choose 1, insert 1 before permute([2,3]), yield [1,2,3], [1,3,2]
    permute([1,2,3]): choose 2, insert 2 before permute([1,3]), yield [2,1,3], [2,3,1]
    permute([1,2,3]): choose 3, insert 3 before permute([1,2]), yield [3,1,2], [3,2,1]
    """
    if len(lst) <= 1:
        yield lst
    else:
        # choose an element in lst
        for i in range(len(lst)):
           # permute the list excluding the chosen element
           for perm in permute(lst[:i] + lst[i+1:]):
               # Insert chosen element into first position of permutation
               yield [lst[i]] + perm

def permute2(lst):
    """
    recursively generate sorted list of all possible permutations of lst
    Same as permute() except doesn't return sorted
    """
    if len(lst) <=1:
        yield lst
    else:
        # loop through every permutation in lst except for first element
        for perm in permute2(lst[1:]):
            # loop through every position in permutation
            for i in range(len(lst)):
                # Insert the first element into every position of permutation
                # equivalent to return perm.insert(i, lst[0])
                yield perm[:i] + [lst[0]] + perm[i:]

def permute_mem(lst):
    """
    recursively return sorted list of all possible permutations of lst.
    Same as permute() except Uses dict to memoize. Not plausible for large data sets (range(11)) due to memory constraint
    """
    if len(lst) <= 1:
        return [lst]
    elif tuple(lst) in mem:
        return mem[tuple(lst)]
    else:
        l = []
        # choose an element in lst
        for i in range(len(lst)):
           # permute the list excluding the chosen element
           for perm in permute_mem(lst[:i] + lst[i+1:]):
               # Insert chosen element into first position of permutation
               l.append([lst[i]] + perm)
        # add to memoization
        mem[tuple(lst)] = l
        return l

def lexinographic_permutation(let, n):
    '''
    returns nth lexinographic permutation of string, 'let'
    using Factorial number system given that items in 'let' are sorted
    '''
    n -= 1
    letters = list(let)
    ret = []
    for i in range(len(letters) - 1, 0, -1):
        fact = math.factorial(i)
        idx = n // fact
##        print(letters)
##        print(n)
##        print(fact)
##        print(idx)
##        print(letters[idx])
        n %= fact
        ret.append(letters.pop(idx))
##        print(ret)
    ret.append(letters.pop(0))
    return ''.join(ret)

def nth_permutation(n):
    '''
    returns nth lexinographic permutation of string, 'let'
    by iterating through all items
    '''
    i = 1
    for p in itertools.permutations(word):
        if i == n:
            return ''.join(p)
        i += 1
                
#for a in permute(range(4)):
#    print(a)
    
#for a in permute2(range(4)):
#    print(a)
    
#for a in permute_mem(range(4)):
#    print(a)
