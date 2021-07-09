import requests
from config import Config
from parser.pokemon import parse_pokemon
from parser.types import parse_type
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
def get_pokemon_by_id(id: int):
    get_pokemon(id)


@app.command()
def get_pokemon_by_name(name: str):
    get_pokemon(name)


def get_pokemon(param):
    res = requests.get(config.baseUrl + f'/pokemon/{param}')
    poke = res.json()
    pokemon = parse_pokemon(poke)
    print(pokemon)

@app.command()
def list_types():
    res = requests.get(config.baseUrl + f'/type')
    types = res.json()
    for t in types['results']:
        print(t['name'])

@app.command()
def get_type(param):
    res = requests.get(config.baseUrl + f'/type/{param}')
    type_json = res.json()
    t = parse_type(type_json)
    print(t)

if __name__ == "__main__":
    app()
