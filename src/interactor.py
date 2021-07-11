import requests
from parser.pokemon import parse_pokemon
from parser.types import parse_type
from parser.item import parse_item
from parser.move import parse_move
from parser.location import parse_location
from img_process.img_transform import ImgTransformer
from logger import log
from config import config


class PokeApiInteractor:
    @staticmethod
    @log
    def get_pokemon(param):
        """get pokemon"""
        res = requests.get(f"{config.base_url}/pokemon/{param}")
        poke = res.json()
        pokemon = parse_pokemon(poke)
        image = ImgTransformer(pokemon.img_url)
        image.save_to_file()
        return pokemon

    @staticmethod
    @log
    def list_types():
        """list all types of pokemons"""
        res = requests.get(f"{config.base_url}/type")
        types = res.json()
        return types

    @staticmethod
    @log
    def get_type(param):
        """get type"""
        res = requests.get(f"{config.base_url}/type/{param}")
        type_json = res.json()
        t = parse_type(type_json)
        return t

    @staticmethod
    @log
    def get_item(param):
        """get item"""
        res = requests.get(f"{config.base_url}/item/{param}")
        item_json = res.json()
        item = parse_item(item_json)
        return item

    @staticmethod
    @log
    def get_move(param):
        """get move"""
        res = requests.get(f"{config.base_url}/move/{param}")
        move_json = res.json()
        move = parse_move(move_json)
        return move

    @staticmethod
    @log
    def get_location(param):
        """get location"""
        res = requests.get(f"{config.base_url}/location/{param}")
        location_json = res.json()
        location = parse_location(location_json)
        return location
