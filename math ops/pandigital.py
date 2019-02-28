def contains_1_of_each(N):
    '''return true if N contains all digits from 1 to len(N) + 1 and no more'''
    return set(str(N)) == set(map(str, range(1, len(str(N)) + 1)))

def contains_1_of_each_digit(N, digits):
    '''return true if N contains all digits listed in digits and no more'''
    if len(str(N)) != len(digits):
        return False
    return set(str(N)) == digits
