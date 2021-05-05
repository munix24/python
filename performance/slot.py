import random
import cProfile
random.seed(1)

pulls=1000000

#generate 8 numbers per pull and score if one is a 7
def build_n_count_bits():
    score=0
    for i in range(pulls):
        for y in range(8):
            if random.getrandbits(3) is 7:
                score+=1
    print(score)

#generate 9 numbers per pull and score if one is a 7
def build_n_count():
    score=0
    for i in range(pulls):
        for y in range(9):
            if random.randrange(0, 10) is 7:
                score+=1
    print(score)
    
#generate 9 numbers per pull and score if one is a 7
def build_n_count2():#slower than random.randrange(0, 10)
    score=0
    for i in range(pulls):
        for y in range(9):
            if random.randint(0, 9) is 7:
                score+=1
    print(score)

#generate 9 numbers per pull and score if one is a 7
#actually builds the arrays
def build_slots_list():
    slots=[]
    sevens=[]
    score=0
    for i in range(pulls):
        slot=[]
        for y in range(9):
            slot.append(random.randint(0, 9))
        slots.append(slot)

    print(slots)
    for i in range(len(slots)):
        count=slots[i].count(7)
        score+=count
        sevens.append(count)
    print(score)
    
cProfile.run('build_n_count_bits()')
#print(random.choice(range(10)))
print(pulls)
