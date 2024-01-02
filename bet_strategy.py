###which strat is highest average wagered based on 10k+ samples
###which strat is highest average max_bal based on 10k+ samples
import random
import cProfile
import statistics

PAYOUT=.98
HOUSE_EDGE=.99
STRAT_CONSTANT=1
STRAT_ALL_IN=2
STRAT_DOBL_ON_LOSS=3
STRAT_HALF_ON_LOSS=4

def sim(bal, bet_bal_ratio, strat):
    if strat==STRAT_CONSTANT:
        bet=max(bal, bal * bet_bal_ratio)
    games=0
    wins=0
    loss=0
    max_bal=0
    wagered=0

    while (bal>0):
        if strat==STRAT_ALL_IN:
            bet=max(bal, bal * bet_bal_ratio)
        if (random.getrandbits(1) == 1):
            bal+=bet * PAYOUT
            wins+=1
            max_bal=max(max_bal, bal)
        else:
            bal-=bet
            loss+=1
        games+=1
        wagered+=bet
    return games, wins, loss, round(wagered), round(max_bal)

def run_sim(num_games=10000, bal_init=10000, bet_bal_ratio=1, strat=STRAT_CONSTANT):
    games_wagered=[]
    games_max_bal=[]

    for _ in range(num_games):
        game=sim(bal_init, bet_bal_ratio, strat)
        games_wagered.append(game[3])
        games_max_bal.append(game[4])
    ##    print(game)
        
    ##print(games_wagered)
    ##print(games_max_bal)
    print('avg_wag=', statistics.mean(games_wagered))
    print('avg_bal=', statistics.mean(games_max_bal))

run_sim()
#cProfile.run('gen_rand_ints()')
