import json
import pandas as pd
import cProfile
from Champ import Champ
from sim_fight import sim_fight
from get_champ_stats import get_champs

pd.set_option('display.max_columns', 14)
pd.set_option('display.width', 0)
pd.set_option('display.max_rows', 200)

def main():
    champions = get_champs()
    champ_instances = {name: Champ(name=name, level=1) for name in champions}
    
    df = pd.DataFrame(index=champions, columns=champions)

    for i, champ1_name in enumerate(champions):
        for j, champ2_name in enumerate(champions):
            if i < j:  # Ensure each pair is considered only once
                champ1 = champ_instances[champ1_name]
                champ2 = champ_instances[champ2_name]
                
                #initialize stats before the fight, in case Champ object is reused
                champ1.hp=champ1.maxhp      
                champ2.hp=champ2.maxhp      
                champ1.attack_cd = 0  
                champ2.attack_cd = 0
                
                winner = sim_fight(champ1, champ2)
##                print(champ1.name, champ1.hp, champ2.name, champ2.hp, winner)
                if winner == 1:
                    df.at[champ1_name, champ2_name] = 1
                    df.at[champ2_name, champ1_name] = 0
                else:
                    df.at[champ1_name, champ2_name] = 0
                    df.at[champ2_name, champ1_name] = 1

##    df.fillna(1, inplace=True)     # Fill NaN values with ''
##    print("Champions winning all fights:", df[df.eq(1).all(axis=1)].index.tolist()) # all wins
##    print("Champions losing all fights:", df[df.eq(0).all(axis=1)].index.tolist())  # all losses
    df['win_%'] = round(df.eq(1).sum(axis=1) / (df.eq(1).sum(axis=1) + df.eq(0).sum(axis=1)) * 100, 2)
    df.sort_values(by=['win_%'], ascending=False, inplace=True)
    
    print(df)
##    print(df.loc['Maokai'])   #Trundle, Tryndamere, Zac, Yuumi
    
if __name__ == "__main__":
    main()
##    cProfile.run('main()', sort='cumulative')
