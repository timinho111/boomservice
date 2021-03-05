import requests


def get_players(team, season):
    url = 'https://v3.football.api-sports.io/players'
    headers = {'x-rapidapi-key': "e6de83259e8d932f70b56603587dcd99"}
    params = {'team': team, 'season': season}
    r = requests.get(url, headers=headers, params=params)
    players = r.json()
    return players
