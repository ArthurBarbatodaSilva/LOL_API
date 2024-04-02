from helpers import get_summoner_info, get_match_ids_by_summoner_puuid, get_match_info

summoner_name = "TFTui"

summoner = get_summoner_info(summoner_name)

name = summoner['name']
level = summoner['summonerLevel']

print(f'name:{name}')
print(f'level:{level}')

summoner_match_ids = get_match_ids_by_summoner_puuid(summoner['puuid'], 20)
print(summoner_match_ids)


matchId = "BR1_2915393879"

match_info = get_match_info(matchId)

for i in range(10):
    nick = match_info['info']['participants'][i]['summonerName']
    champion = match_info['info']['participants'][i]['championName']
    
    print(f'nick:{nick}, champion:{champion}')



