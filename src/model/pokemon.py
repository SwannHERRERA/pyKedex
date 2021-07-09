class Pokemon:
    def __init__(self, name, speed, attack, life, img_url, types, moves, weight):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.life = life
        self.img_url = img_url
        self.types = types
        self.moves = moves
        self.weight = weight

    def __str__(self):
        pokemon = f'''
name: {self.name}
speed: {self.speed}
attack: {self.attack}
life: {self.life}
weight: {self.weight}
'''
        pokemon += self.types_to_string()
        pokemon += '\n'
        pokemon += self.moves_to_string()
        return pokemon

    def types_to_string(self):
        s = 'types: [ '
        for name in self.types:
            s += f'{name} '
        s += ' ]\n'
        return s
    
    def moves_to_string(self):
        s = 'moves: [ '
        for name in self.moves:
            s += f'{name} '
        s += ' ]\n'
        return s
    