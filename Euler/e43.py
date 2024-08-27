import itertools

nums=list(range(0,10))
nums=map(str,nums)
#print(nums)

def sub_string_divisibility_property(num):
    st = str(num)
    #print(st)
    #print(int(st[1:4]))
    if int(st[1:4]) % 2:
        return False
    if int(st[2:5]) % 3:
        return False
    if int(st[3:6]) % 5:
        return False
    if int(st[4:7]) % 7:
        return False
    if int(st[5:8]) % 11:
        return False
    if int(st[6:9]) % 13:
        return False
    if int(st[7:10]) % 17:
        return False
    return True

num=1406357289
nums_w_property=[]

for num2 in itertools.permutations(nums):
    num = list(num2)
    num = ''.join(num2)
##    print(num)
    if sub_string_divisibility_property(num):
        nums_w_property.append(int(num))
        #print(nums_w_property)

print(sum(nums_w_property))
