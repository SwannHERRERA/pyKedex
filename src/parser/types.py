from model.type import Type

def parse_type(type_json):
  name = type_json['name']
  generation = type_json['generation']['name']
  pokemons = [pokemon['pokemon']['name'] for pokemon in type_json['pokemon']] 
  moves = [move['name'] for move in type_json['moves']]
  types_relations = {
    'x2to': [double_damage_to['name'] for double_damage_to in type_json['damage_relations']['double_damage_to']],
    'x2from': [double_damage_from['name'] for double_damage_from in type_json['damage_relations']['double_damage_from']],
    '/2to': [half_damage_to['name'] for half_damage_to in type_json['damage_relations']['half_damage_to']],
    '/2from': [half_damage_from['name'] for half_damage_from in type_json['damage_relations']['half_damage_from']],
    'x0to': [no_damage_to['name'] for no_damage_to in type_json['damage_relations']['no_damage_to']],
    'x0form': [no_damage_from['name'] for no_damage_from in type_json['damage_relations']['no_damage_from']],
  }
  return Type(name, generation, types_relations, pokemons, moves)