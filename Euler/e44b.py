import math
import time
import cProfile

def quad_equation(a,b,c):   
    dis = (b**2) - (4 * a*c)
    #ans1 = (-b-math.sqrt(dis))/(2 * a)
    ans2 = (-b + math.sqrt(dis))/(2 * a)
    return ans2    #return positive answer

def is_pentagonal(n):
    return quad_equation(3,-1,-n*2) % 1 < .0000001

def pentagonal_reverse(n):
    return quad_equation(3,-1,-n*2)

def pentagonal(i):
    return int(i*(3*i-1)/2)

def pentagonals_create(limit):
    pentagonals=[]
    pentagonals2=set()
    pentagonals3={}
    for _ in range(1, limit):
        pentagonals.append(pentagonal(_))
        pentagonals2.add(pentagonal(_))
        pentagonals3[_]=pentagonal(_)
    return pentagonals,pentagonals2,pentagonals3

def increase(i):
    return 3*i + 1

def max_index(n):
    return int((n - 1)/3)+1

def find_pens(limit):
    pentagonals,pentagonals2,pentagonals3 = pentagonals_create(limit)
    len_pen3=len(pentagonals3)
##    print(pentagonals)

    start = time.time()
    for mn in range(1,47000):
    ##    mx = max_index(pentagonals[mn-1])
    ##    mx = min(90000, max_index(pentagonal(mn)))
        if not mn % 1000:
            print(mn,int(time.time()-start))
            start = time.time()
            
        mn_pen=pentagonals3[mn]
        for j in range(mn+1, len_pen3):
##            k=pentagonal_reverse(k_pen)
##            if k % 1 < .00001:
            k_pen=(mn_pen+pentagonals3[j])
            if k_pen in pentagonals2:
                top=pentagonal_reverse(pentagonals3[j]+k_pen)
                if top % 1 < .00001:
                    print(mn, j, pentagonal_reverse(k_pen), top)
                    print(pentagonal(mn), pentagonal(j), k_pen, pentagonal(top))
                    print(k_pen-pentagonal(j))

find_pens(990000)
##cProfile.run('find_pens(1000)')

##10000-1
##9999+9998+9997
##(n^2 + n)/2
##increases by 3n+1
##for every pen check 

##store all diffs in list
##store all sums in list
##if diff is pen then get j,k and check if sum is pen
##add diffs and check if pen then get j,k and check if sum is pen
