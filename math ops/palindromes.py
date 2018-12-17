import math

def is_palindrome(string):
    return string == string[::-1]

def gen_palindromes2(limit): # using integer operators
    for num in range(1, limit + 1):
        temp = num
        reverse = 0
        
        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10

        if(num == reverse):
            print("%d " %num, end = '  ')

def gen_palindromes(limit):
    max_length = math.ceil(math.log10(limit))
##    print(max_length)
    for length in range(1, max_length + 1):
        if length == 1:
            for a in range(1, 10):
                if a < limit:
                    yield a
            continue
        for a in range(10 ** ((length - 2) // 2), 10 ** (length // 2)):
##            if length == max_length:
##                print(a * 10 ** (length // 2), a, length, limit)
##                if a * 10 ** (length // 2)  > limit:
##                    break
            if length % 2 == 0: # even
                ret = int(str(a) + str(a)[::-1])
                if ret < limit:
                    yield ret
            if length % 2:  # odd
                for b in range(10):
                    ret = int(str(a) + str(b) + str(a)[::-1])
                    if ret < limit:
                        yield ret
                    
def list_palindromes(limit):
    ret = []
    for p in gen_palindromes(limit):
        ret.append(p)
    return ret

##N = 1000

##ret = list_palindromes(N)
##print(ret)

