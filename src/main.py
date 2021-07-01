import requests
from config import Config
config = Config('https://pokeapi.co/api/v2')

def getPokemons():
  res = requests.get(config.baseUrl + '/pokemon')
  pokes = res.json()
  print(pokes['count'])
  print(pokes['results'][5]['name'])

getPokemons()
