from flask import Flask, render_template
from helpers import get_summoner_info, get_match_ids_by_summoner_puuid, get_match_info
import requests
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/api/match/<string:userInput>/<string:userInputTag>/<string:gamesUser>', methods=['GET'])

#Acessando os dados da partida atráves do summonerName e Tagline
#O Data Dragon ou ddragon é o conjunto de arquivos de dados estáticos que fornece imagens e informações dos campeões,runas e itens


def get_matches(userInput, userInputTag, gamesUser):
    summoner_name = userInput
    tagline = userInputTag
    games = gamesUser
    summoner = get_summoner_info(summoner_name, tagline)
    summoner_match_ids = get_match_ids_by_summoner_puuid(summoner['puuid'], games) 
    data = []

    for matchId in summoner_match_ids:
        match_info = get_match_info(matchId)

        for i in range(10):
            participant = match_info['info']['participants'][i]
            nick = participant['summonerName']
            champion = participant['championName']
            kills = participant['kills']
            deaths = participant['deaths']
            assists = participant['assists']
            score = get_kda(participant)
            minion = participant['totalMinionsKilled']
            team = participant['teamId']
            icon = f'https://ddragon.leagueoflegends.com/cdn/14.9.1/img/champion/{champion}.png'

            champion_items = []
            items_icons = []
            runes_icons = []

            for item_index in range(6):
                item_key = f"item{item_index}"
                if item_key in participant:
                    champion_items.append(participant[item_key])
                    item_id = champion_items[-1]
                    item_icon_url = f'https://ddragon.leagueoflegends.com/cdn/14.9.1/img/item/{item_id}.png'
                    items_icons.append(item_icon_url)

            for style in participant['perks']['styles']:
                for selection in style['selections']:
                    rune_id = selection['perk']
                    if rune_id in rune_dict:
                        rune_icon_url = f"https://ddragon.leagueoflegends.com/cdn/img/{rune_dict[rune_id]}"
                        runes_icons.append(rune_icon_url)


            data.append({
                "nick": nick,
                "champion": champion,
                "team": team_color(team),
                "icon": icon,
                "score": score,
                "items": champion_items,
                "kills": kills,
                "deaths": deaths,
                "assists": assists,
                "minion": minion,
                "items_icons": items_icons,
                "runes_icons": runes_icons,
                "stats": participant,
            })

    return render_template('home.html', data=data)


def team_color(team):
    if team == 100:
        return 'Azul'
    if team == 200:
        return 'Vermelho'
    

def ddragon_get_runes_dict():
    url = "http://ddragon.leagueoflegends.com/cdn/14.9.1/data/en_US/runesReforged.json"
    runes_data = requests.get(url).json()
    rune_dict = {}
    for tree in runes_data:
        for slot in tree["slots"]:
            for rune in slot["runes"]:
                rune_dict[rune["id"]] = rune["icon"]
    return rune_dict

rune_dict = ddragon_get_runes_dict()

def get_kda(participant):
    kda = participant.get('challenges', {}).get('kda')
    
    if kda is None:
        kda = participant.get('kda', 0)  # Usa 0 como padrão se participant['kda'] não existir
    return round(kda, 3)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
