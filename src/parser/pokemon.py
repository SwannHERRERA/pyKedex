from model.pokemon import Pokemon

def parse_pokemon(pokemon_json):
  name = pokemon_json['name']
  weight = pokemon_json['weight']
  for stat in pokemon_json['stats']:
    if stat['stat']['name'] == 'speed':
      speed = stat['base_stat']
    if stat['stat']['name'] == 'hp':
      life = stat['base_stat']
    if stat['stat']['name'] == 'attack':
      attack = stat['base_stat']
    
  types = [typ['type']['name'] for typ in pokemon_json['types']]
  moves = [move['move']['name'] for move in pokemon_json['moves']]
  img_url = f'https://img.pokemondb.net/sprites/home/normal/{name.lower()}.png'
  return Pokemon(name, speed, attack, life, img_url, types, moves, weight)