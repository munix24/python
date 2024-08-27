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

pentagonals=[1,5,12,22,35]
D=0
mn=5

while D==0:
##    mx = max_index(pentagonals[mn-1])
    mx = min(100000, max_index(pentagonal(mn)))
    j=mn+1
##    print(mn,j,mx)
    if not mn % 1000:
        print(mn,j,mx) 
    while j <= mx:
##        print(mn,j,mx)
##        print(pentagonals)
##        if len(pentagonals) <= j:
##            pentagonals.append(pentagonal(j))
##        k=pentagonal_reverse(pentagonals[mn-1]+pentagonals[j-1])
        k=pentagonal_reverse(pentagonal(mn)+pentagonal(j))                               
        if k % 1 < .00001:
            k=int(k)
##            print(len(pentagonals))
##            print(pentagonals)
##            print(k)
            top=pentagonal_reverse(pentagonal(j)+pentagonal(k))
##            print(mn, j, k, top)
##            print(pentagonal(mn), pentagonal(j), pentagonal(k), pentagonal(j)+pentagonal(k))
##            print(top)
            if top % 1 < .00001:
                print(mn, j, k, top)
                print(pentagonal(mn), pentagonal(j), pentagonal(k), pentagonal(top))
                print(pentagonal(k)-pentagonal(j))
            break
##        if is_pentagonal(pentagonals[mn]+pentagonals[j]):
        j+=1
        
    mn+=1
##    print(pentagonals)
    

#3/2n^2-1/2n
