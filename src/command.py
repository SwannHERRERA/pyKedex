from interactor import PokeApiInteractor
from main import config
import webbrowser


@app.command()
def get_pokemon_by_id(id: int):
    pokemon = PokeApiInteractor.get_pokemon(id)
    print(pokemon)
    webbrowser.open(config.img_path)


@app.command()
def get_pokemon_by_name(name: str):
    pokemon = PokeApiInteractor.get_pokemon(name)
    print(pokemon)
    webbrowser.open(config.img_path)


@app.command()
def list_pokemons():
    """"""


@app.command()
def list_types():
    types = PokeApiInteractor.list_types()
    for t in types["results"]:
        print(t["name"])


@app.command()
def get_move(identifier):
    move = PokeApiInteractor.get_move(identifier)
    print(move)


@app.command()
def get_location(identifier):
    location = PokeApiInteractor.get_location(identifier)
    print(location)


@app.command()
def get_item(identifier):
    item = PokeApiInteractor.get_item(identifier)
    print(item)


@app.command()
def get_type(identifier):
    typ = PokeApiInteractor.get_type(identifier)
    print(typ)
