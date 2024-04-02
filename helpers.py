import requests
from urllib.parse import urlencode
import settings


def get_summoner_info(summoner_name=None, region=settings.DEFAULT_REGION_CODE):
    """conseguindo informações da conta atráves do nome do invocador"""

    if not summoner_name:
        summoner_name = input("summoner name:")

    params = {
        'api_key': settings.API_KEY
    }

    api_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"

    "fazendo um tratamento de erro ,caso ocorra algum, mostrar uma mensagem de erro "
    "solicitação sendo feita á API na linha 26, passando o parametro e a API_KEY "
    "usando urlencode para converter o conteudo dentro do params em formato de URL"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Problema ao conseguir os dados do invocador pela API:{e}")
        return None


def get_match_ids_by_summoner_puuid(summoner_puuid, matches_count, region=settings.DEFAULT_REGION):

    """ retornando uma lista do histórico de partidas atráves do puuid so invocador"""

    params = {
        'api_key': settings.API_KEY,
        'count': matches_count,
    }

    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids"
    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Problema ao conseguir os dados do invocador pela API: {e}')
        return None

def get_match_info(match_id, region=settings.DEFAULT_REGION ):

    params = {
        'api_key': settings.API_KEY,
    }

    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    try:
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Problema ao conseguir os dados do invocador pela API: {e}')
        return None