from model.move import Move


def parse_move(move_json):
    name = move_json["name"]
    typ = move_json["type"]["name"]
    power = move_json["power"]
    accuracy = move_json["accuracy"]
    pokemons = [pokemon["name"] for pokemon in move_json["learned_by_pokemon"]]
    return Move(name, typ, power, accuracy, pokemons)
