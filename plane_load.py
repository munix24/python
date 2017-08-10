'''
TODO
research historical manifest log, pull CG and optimal CG,  and calculate cost savings if containers were loaded optimally.
how is CG/optimal CG measured?
min, max CG depends on plane and TOW/ZFW. where is envelope data per plane?

PROBLEM
https://en.wikipedia.org/wiki/Center_of_gravity_of_an_aircraft
The center of gravity (CG) of an aircraft is the point over which the aircraft would balance. CG is an important 
point on an aircraft, which significantly affects the stability of the aircraft. To ensure the aircraft is stable 
enough to be safe to fly, the center of mass must fall within specified limits.

given an array of container weights R of size N and an array of position max weight K of size P
For every position K print a container weight, R, that doesn't exceed K such that the heaviest containers are in the back.
Once a container is used it containernot be used again. If no available container fits in a position, print 0 for that position.

Input
One line with two integers N: the number of containers, and P, the number of positions.
One line with N integers Ri. The i-th of these represents the weight of the container.
One line with P integers Ki. The i-th of these represents the maximum weight a position container support.

Output
One line with N integers Ri. The i-th of these represents the 

Limits
1 ≤ N ≤ 50
1 ≤ P ≤ 50
1 ≤ Ri ≤ 10000
1 ≤ Ki ≤ 10000
'''
tc1='''3 3
1 2 3
3 3 3'''
tc2='''4 4
3 4 5 6
4 5 5 4'''
tc3='''5 5
3 3 4 6 6
4 5 3 2 9'''

def autoload(input):
    lines=input.split('\n')
    N,P=lines[0].split()
    R=list(map(int,lines[1].split()))
    K=list(map(int,lines[2].split()))
    R.sort()
    ret=""
    for k in reversed(K):
        for r in reversed(R):
            if r<=k:
                ret=str(r) + " " + ret
                R.remove(r)
                break
            elif r==R[0]:
                ret="0 " + ret  #no match found
                break
    return ret

print(autoload(tc1))
print(autoload(tc2))
print(autoload(tc3))
