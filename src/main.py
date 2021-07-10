import requests
from config import Config
from parser.pokemon import parse_pokemon
from parser.types import parse_type
from parser.item import parse_item
from parser.move import parse_move
from parser.location import parse_location
import typer

app = typer.Typer()
config = Config("https://pokeapi.co/api/v2")


@app.command()
def get_pokemons():
    res = requests.get(config.baseUrl + "/pokemon")
    pokes = res.json()
    print(pokes["count"])
    print(pokes["results"][5]["name"])


@app.command()
def get_pokemon_by_id(id: int):
    get_pokemon(id)


@app.command()
def get_pokemon_by_name(name: str):
    get_pokemon(name)


def get_pokemon(param):
    res = requests.get(config.baseUrl + f"/pokemon/{param}")
    poke = res.json()
    pokemon = parse_pokemon(poke)
    print(pokemon)


@app.command()
def list_types():
    res = requests.get(config.baseUrl + f"/type")
    types = res.json()
    for t in types["results"]:
        print(t["name"])


@app.command()
def get_type(param):
    res = requests.get(config.baseUrl + f"/type/{param}")
    type_json = res.json()
    t = parse_type(type_json)
    print(t)


@app.command()
def get_item(param):
    res = requests.get(config.baseUrl + f"/item/{param}")
    item_json = res.json()
    item = parse_item(item_json)
    print(item)


@app.command()
def get_move(param):
    res = requests.get(config.baseUrl + f"/move/{param}")
    move_json = res.json()
    move = parse_move(move_json)
    print(move)


@app.command()
def get_location(param):
    res = requests.get(config.baseUrl + f"/location/{param}")
    location_json = res.json()
    location = parse_location(location_json)
    print(location)


if __name__ == "__main__":
    app()
