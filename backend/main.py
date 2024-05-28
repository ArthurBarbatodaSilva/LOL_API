from helpers import get_summoner_info, get_match_ids_by_summoner_puuid, get_match_info
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/match':
            summoner_name = "TFTui"
            summoner = get_summoner_info(summoner_name)
            summoner_match_ids = get_match_ids_by_summoner_puuid(summoner['puuid'], 1)
            matchId = summoner_match_ids[0] if summoner_match_ids else "BR1_2943062901"
            match_info = get_match_info(matchId)

            data = []

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
                        item_id = champion_items[-1]
                        item_icon_url = f'https://ddragon.leagueoflegends.com/cdn/14.9.1/img/item/{item_id}.png'
                        items_icons.append(item_icon_url)

                data.append({
                    "nick": nick,
                    "champion": champion,
                    "team": team,
                    "icon": icon,
                    "items": champion_items,
                    "items_icons": items_icons
                })

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
