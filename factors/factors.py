prod_last = {}
for i in range(10):
    prod_last[str(i)] = []
    
for i in range(10):
    for n in range(10):
        prod_last_dig=str(i * n)[-1]
        prod_last[prod_last_dig].append([i, n])

for i in range(10):
    print(i, prod_last[str(i)])

prime1=33
prime2=11
##prime1=999
##prime2=999
##semiprime=12321
semiprime = prime1*prime2
print(semiprime)

possibilities=[]
for poss in prod_last[str(semiprime)[-1]]:
    possibilities.append(poss)

for i in range(-2, -(len(str(semiprime))+1), -1):
    dig=int(str(semiprime)[i])
##for dig in map(int, reversed(str(semiprime)[:-1])):   #loop through digits in semiprime
    print(possibilities)
    print(dig)
    for _ in range(len(possibilities)):
        poss=possibilities.pop()
        if poss[0]*poss[1] == semiprime:
            print('factors: ', poss[0],poss[1])
            break
        print(poss)
        
        remainder=str(poss[0]*poss[1])[:i+1]
        remainder = int(remainder) if remainder != "" else 0
        print(remainder)

        if dig > remainder or dig == remainder:
            dig_act = str(dig - remainder)
        else:
            dig_act = str(10 + dig - remainder) #dig_act will need to go to next
        print(dig_act)

        for a in range(10):
            for b in range(10):
                fact1 = int(str(a) + str(poss[0]))
                fact2 = int(str(b) + str(poss[1]))
                fact_prod = fact1 * fact2
                if fact_prod > semiprime:
                    continue
                if str(fact_prod)[i:] == str(semiprime)[i:]:
                    print(fact1, fact2, fact_prod)
                    possibilities.insert(0, [fact1, fact2, fact_prod])

##        possible_factors=prod_last[dig_act]
##        print('possible_factors')
##        print(possible_factors)
##
##        for poss_factors in possible_factors:
##            poss_factor0=poss_factors[0]
##            poss_factor1=poss_factors[1]
##            print(str(poss_factor0)+str(poss[0]))
##
##            poss_new=[str(poss_factor0)+str(poss[0]), str(poss_factor1)+str(poss[1])]
##            print(poss_new)
##            possibilities.insert(0, poss_new)
##    for possibilities in prod_last[str(prod)[dig]]:
        
def random_add(dig_act):
    return
