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
    recursively generate list of all possible permutations of lst. Returned list is out of sort.
    permute([2,3]): permute([3]) yields [3], insert 2 before and after 3 and yield [2,3], [3,2]
    permute([1,2,3]): permute([2,3]): yields [2,3], [3,2] (see above)
    permute([1,2,3]): insert 1 at every position of [2,3] yielding [1, 2, 3], [2, 1, 3], [2, 3, 1]
    permute([1,2,3]): insert 1 at every position of [3,2] yielding [1, 3, 2], [3, 1, 2], [3, 2, 1]
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
                
for a in permute(range(2,4)):
    print(a)
    
#for a in permute2(range(1,4)):
#    print(a)
