def contains_1_of_each_digit(N, digits):
    '''return true if N contains all digits listed in digits and no more'''
    if len(str(N)) != len(digits):
        return False
    digs = set()
    for n in str(N):
        digs.add(n)
    return digs == digits
