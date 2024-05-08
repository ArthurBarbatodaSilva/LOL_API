from helpers import get_summoner_info, get_match_ids_by_summoner_puuid, get_match_info

summoner_name = "Seryu Ubiquitous"

summoner = get_summoner_info(summoner_name)

#name = summoner['name']
#level = summoner['summonerLevel']

#print(f'name:{name}')
#print(f'level:{level}')
print(summoner)

summoner_match_ids = get_match_ids_by_summoner_puuid(summoner['puuid'], 20)
print(summoner_match_ids)


matchId = "BR1_2934823376"

match_info = get_match_info(matchId)



for i in range(10):
    nick = match_info['info']['participants'][i]['summonerName']
    champion = match_info['info']['participants'][i]['championName']
    team = match_info['info']['participants'][i]['teamId']
    icon = f'https://ddragon.leagueoflegends.com/cdn/14.9.1/img/champion/{champion}.png'
    
    champion_items = []
    items_icons = []

    for item_index in range(6):
        item_key = f"item{item_index}"  
        if item_key in match_info['info']['participants'][i]:
            champion_items.append(match_info['info']['participants'][i][item_key])
            item_id = champion_items[-1]  # Access the latest appended item ID
            item_icon_url = f'https://ddragon.leagueoflegends.com/cdn/14.9.1/img/item/{item_id}.png'
            items_icons.append(item_icon_url)

            
    
    print(f"\033[32mnick:{nick}\033[0m,\033[34mchampion:{champion}\033[0m,\033[37micon:{icon}\033[0m, team:{team}, \033[33mitem:{champion_items}\033[0m")
    print(f"\033[31mitems-Icons:{items_icons}\033[0m")

