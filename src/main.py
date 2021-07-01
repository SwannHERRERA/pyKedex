import requests
from config import Config

config = Config('https://pokeapi.co/api/v2/')

def getPokemons():
  pokes = requests.get(config.baseUrl + '/pokemons')
  print(pokes)

getPokemons()