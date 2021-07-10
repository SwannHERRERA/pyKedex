class Move:
    def __init__(self, name, mTtype, power, accuracy, pokemons):
        self.name = name
        self.type = mTtype
        self.power = power
        self.accuracy = accuracy
        self.pokemons = pokemons

    def __str__(self):
        return (
            f"""
move: {self.name}
type: {self.type}
power: {self.power}
accuracy: {self.accuracy}
"""
            + self.get_pokemons()
        )

    def get_pokemons(self):
        res = "eligible pokemons: [ "
        for poke in self.pokemons:
            res += f"{poke} "
        res += "]"
        return res
