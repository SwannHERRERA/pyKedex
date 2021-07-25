from interactor import PokeApiInteractor
from config import config
import webbrowser
import typer
from logger import logger

app = typer.Typer()


@app.command()
def get_pokemon_by_id(id: int):
    pokemon = PokeApiInteractor.get_pokemon(id)
    if pokemon is None:
        return
    print(pokemon)
    webbrowser.open(config.image_path)


@app.command()
def get_pokemon_by_name(name: str):
    pokemon = PokeApiInteractor.get_pokemon(name)
    if pokemon is None:
        return
    print(pokemon)
    webbrowser.open(config.image_path)


@app.command()
def get_evolution(identifier):
    evolution = PokeApiInteractor.get_evolution(identifier)
    if evolution is None:
        return
    print(evolution)


@app.command()
def list_pokemons(page_indice):
    pokemons = PokeApiInteractor.list_pokemons(page_indice)
    if pokemons is None:
        return
    print("number total of pokemon: " + str(pokemons["count"]))
    for pokemon in pokemons["results"]:
        print(pokemon["name"])


@app.command()
def list_types():
    types = PokeApiInteractor.list_types()
    if types is None:
        return
    for t in types["results"]:
        print(t["name"])


@app.command()
def get_move(identifier):
    move = PokeApiInteractor.get_move(identifier)
    if move is None:
        return
    print(move)


@app.command()
def get_location(identifier):
    location = PokeApiInteractor.get_location(identifier)
    if location is None:
        return
    print(location)


@app.command()
def get_item(identifier):
    item = PokeApiInteractor.get_item(identifier)
    if item is None:
        return
    print(item)


@app.command()
def get_type(identifier):
    typ = PokeApiInteractor.get_type(identifier)
    if typ is None:
        return
    print(typ)


@app.command()
def get_actions():
    actions = logger.get_actions()
    print(actions)


@app.command()
def get_all_actions():
    actions = logger.get_all_actions()
    print(actions)


@app.command()
def get_errors():
    actions = logger.get_errors()
    print(actions)
