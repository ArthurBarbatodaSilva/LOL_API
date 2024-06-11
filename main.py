from flask import Flask, render_template
from helpers import get_summoner_info, get_match_ids_by_summoner_puuid, get_match_info

app = Flask(__name__)

@app.route('/api/match/<string:userInput>', methods=['GET'])
def get_matches(userInput):
    summoner_name = userInput
    summoner = get_summoner_info(summoner_name)
    summoner_match_ids = get_match_ids_by_summoner_puuid(summoner['puuid'], 10) 
    data = []

    for matchId in summoner_match_ids:
        match_info = get_match_info(matchId)

        for i in range(10):
            participant = match_info['info']['participants'][i]
            nick = participant['summonerName']
            champion = participant['championName']
            team = participant['teamId']
            icon = f'https://ddragon.leagueoflegends.com/cdn/14.9.1/img/champion/{champion}.png'

            champion_items = []
            items_icons = []

            for item_index in range(6):
                item_key = f"item{item_index}"
                if item_key in participant:
                    champion_items.append(participant[item_key])
                    item_id = champion_items[-1]
                    item_icon_url = f'https://ddragon.leagueoflegends.com/cdn/14.9.1/img/item/{item_id}.png'
                    items_icons.append(item_icon_url)

            data.append({
                "nick": nick,
                "champion": champion,
                "team": team_color(team),
                "icon": icon,
                "items": champion_items,
                "items_icons": items_icons,
                "stats": participant  # Adicionando informações de estatísticas completas
            })

    return render_template('home.html', data=data)

def team_color(team):
    if team == 100:
        return 'Azul'
    if team == 200:
        return 'Vermelho'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
