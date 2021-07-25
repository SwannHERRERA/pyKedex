from parser.item import parse_item
from parser.location import parse_location
from parser.move import parse_move
from parser.pokemon import parse_pokemon
from parser.types import parse_type
from parser.evolution import parse_evolve

import requests

from config import config
from img_process.img_transform import ImgTransformer
from logger import log, logger


class PokeApiInteractor:
    @staticmethod
    @log
    def list_pokemons(page):
        """list pokemons with pagination (step of 20)"""
        try:
            res = requests.get(
                f"{config.base_url}/pokemon?offset={int(page)*20}&limit=20"
            )
            pokes = res.json()
            return pokes
        except:
            print("Erreur lors de la récupération des pokemons")

    @staticmethod
    @log
    def get_pokemon(param):
        """get pokemon"""
        try:
            res = requests.get(f"{config.base_url}/pokemon/{param}")
            poke = res.json()
        except:
            logger.log_error(f"Erreur lors de la récupération du pokemon {param}")
            return
        pokemon = parse_pokemon(poke)
        image = ImgTransformer(pokemon.img_url)
        image.save_to_file()
        return pokemon

    @staticmethod
    @log
    def get_evolution(param):
        """get evolution"""
        try:
            res = requests.get(f"{config.base_url}/pokemon/{param}")
            poke = res.json()
            specie_url = poke["species"]["url"]
            res_specie = requests.get(specie_url)
            specie = res_specie.json()
            evolution_chain_url = specie["evolution_chain"]["url"]
            res_evolution_chain = requests.get(evolution_chain_url)
            row_evolution_chain = res_evolution_chain.json()
            evolution_chain = parse_evolve(row_evolution_chain)
            return evolution_chain
        except:
            logger.log_error(
                f"Erreur lors de la récupération de la chaine d'évolution du pokemon {param}"
            )
            return

    @staticmethod
    @log
    def list_types():
        """list all types of pokemons"""
        try:
            res = requests.get(f"{config.base_url}/type")
        except:
            logger.log_error("Erreur lors de la récupération des types")
            return
        types = res.json()
        return types

    @staticmethod
    @log
    def get_type(param):
        """get type"""
        try:
            res = requests.get(f"{config.base_url}/type/{param}")
        except:
            logger.log_error(f"Erreur lors de la récupération du type {param}")
            return
        type_json = res.json()
        t = parse_type(type_json)
        return t

    @staticmethod
    @log
    def get_item(param):
        """get item"""
        try:
            res = requests.get(f"{config.base_url}/item/{param}")
        except:
            logger.log_error(f"Erreur lors de la récupération de l'item {param}")
            return
        item_json = res.json()
        item = parse_item(item_json)
        return item

    @staticmethod
    @log
    def get_move(param):
        """get move"""
        try:
            res = requests.get(f"{config.base_url}/move/{param}")
        except:
            logger.log_error(f"Erreur lors de la récupération du move {param}")
            return
        move_json = res.json()
        move = parse_move(move_json)
        return move

    @staticmethod
    @log
    def get_location(param):
        """get location"""
        try:
            res = requests.get(f"{config.base_url}/location/{param}")
        except:
            logger.log_error(f"Erreur lors de la récupération de la location {param}")
            return
        location_json = res.json()
        location = parse_location(location_json)
        return location
