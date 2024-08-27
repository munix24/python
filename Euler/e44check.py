import math

def quad_equation(a,b,c):   
    dis = (b**2) - (4 * a*c)
    ans1 = (-b-math.sqrt(dis))/(2 * a)
    ans2 = (-b + math.sqrt(dis))/(2 * a)
    return ans2    #return positive answer

def is_pentagonal(n):
    return quad_equation(3,-1,-n*2) % 1 < .0000001

def pentagonal_reverse(n):
    return quad_equation(3,-1,-n*2)

def pentagonal(i):
    return int(i*(3*i-1)/2)

def increase(i):
    return 3*i + 1

def max_index(n):
    return int((n - 1)/3)+1

mn=55500
j=95506
k=110461
mn=46303
j=111972
k=121168
print(mn,j,k,pentagonal_reverse(pentagonal(k)+pentagonal(j)))
print(pentagonal(mn),pentagonal(j),pentagonal(k),pentagonal(pentagonal_reverse(pentagonal(k)+pentagonal(j))))
print(pentagonal(k)-pentagonal(j))
