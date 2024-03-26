import time
##import bisect
##py 3.10 is needed to insort using key ##bisect.insort(attack_queue, (attacker.attack_cd, attacker, attacked))
from collections import deque
from Champ import Champ

#1m runs of deque vs list perf is nearly the same ~5s
def sim_fight(champ1, champ2, print_actions=0):  
    attack_queue = deque([(0, champ1, champ2), (0, champ2, champ1)])
    attack_queue = deque(sorted(attack_queue, key=lambda x: x[0]))

    while attack_queue and not champ1.is_defeated() and not champ2.is_defeated():
        current_time, attacker, attacked = attack_queue.popleft()
        attacker.attack(attacked)
        if print_actions:
            print(f"{current_time:.2f}s: {attacked.name} took {attacker.attackdamage} damage. {attacked.name}'s HP: {attacked.hp}")
        attack_queue.append((attacker.attack_cd, attacker, attacked))
        attack_queue = deque(sorted(attack_queue, key=lambda x: x[0]))

    if champ1.is_defeated():
        return 2
    else:
        return 1

##print(vars(champ2))
if __name__ == "__main__":
    champ1 = Champ(name="Annie", level=1)
    champ2 = Champ(name="Anivia", level=1)

##    print(champ1.stats)
##    print(champ2.stats)

    start_time = time.time()
    winner = sim_fight(champ1, champ2, 1)
    if winner == 1:
        print(f"{champ1.name} wins the battle! Remaining HP: {champ1.hp}")
    else:
        print(f"{champ2.name} wins the battle! Remaining HP: {champ2.hp}")

    print(f"Simulation took {time.time() - start_time:.4f} seconds to finish.")

