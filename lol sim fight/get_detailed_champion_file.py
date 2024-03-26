import json
import pandas as pd
from urllib.request import urlopen
##import requests

pd.set_option('display.max_columns', 14)
pd.set_option('display.width', 0)
pd.set_option('display.max_rows', 200)

with open('championFull.json', encoding='utf-8') as f:
    data = json.load(f)
champion_names = data['keys'].values()

url = 'https://raw.communitydragon.org/latest/game/data/characters/'

for champion in champion_names:
    champion_url = url + champion + '/' + champion + '.bin.json'
    print(champion_url)
    response = urlopen(champion_url)
##    source = requests.get(champion_url).json()
##    print(source)
    data_json = json.loads(response.read()) 
    print(data_json)
    exit()

    

####print(champion_data)
####features=['summonerName', 'summonerLevel', 'individualPosition', 'championId', 'championName', 'teamEarlySurrendered', 'gameEndedInSurrender', 'win']
##
####print(champion_data['Aatrox'])
##table_data = [] # list of dicts
##for champion in champion_data.values():
##    champ={'name':champion['id']}
##    champ.update(champion['stats'])
##    table_data.append(champ)
##    
##df = pd.DataFrame(table_data)
##df.set_index('name', inplace=True)     # Set Champion Name as index
##
##def get_champ_stats(champ):
##    return df.loc[champ]
##
##def get_champs():
##    return data['data'].keys()
##
##if __name__ == "__main__":
##    ##print(table_data)
####    print(df)
##    print(df.loc["Aatrox"])
##    ##print(get_champ_stats('Aatrox'))

