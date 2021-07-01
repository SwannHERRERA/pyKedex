import requests
from config import Config
import typer

app = typer.Typer()
config = Config('https://pokeapi.co/api/v2')

@app.command()
def get_pokemons():
  res = requests.get(config.baseUrl + '/pokemon')
  pokes = res.json()
  print(pokes['count'])
  print(pokes['results'][5]['name'])

@app.command()
def get_pokemon():
  id = 4
  res = requests.get(config.baseUrl + f'/pokemon/{id}')
  pokes = res.json()
  print(pokes['name'])
  print(pokes['types'][0]['type']['name'])
  print(pokes['weight'])
  print("{}: {}".format(pokes['stats'][0]['stat']['name'], pokes['stats'][0]['base_stat']))

if __name__ == "__main__":
    app()