def concatenate_int_list(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

'''
key is the sum of digits of possible multiplicants and product,
value is digit length of multiplicants
'''
multiplicants_for_total_digit_sum = {
    10: [[1, 4], [2, 3]],
    9: [[1, 4], [2, 3]],
    8: [[1, 3], [2, 2]],
    7: [[1, 3], [2, 2]],
    6: [[1, 2]],
    5: [[1, 2]],
    4: [[1, 1]]
    }

'''
lookup product digit len to identify the possible digit len of its multiplicants

product dig len has to be a summand of two nonzero integers or possibly 1 over.

example: 10 
'''

multiplicants_for_product_digits = {
    1: [[1, 1]],
    2: [[1, 1], [1, 2]],
    3: [[1, 2], [2, 2], [1, 3]],
    4: [[2, 2], [1, 3]],
    5: [[2, 3], [1, 4], [3, 3], [4, 2], [1, 5]]
    }