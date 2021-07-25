class EvolutionChain:
    def __init__(self, pokemons):
        self.pokemons = pokemons

    def __str__(self):
        if len(self.pokemons) == 1:
            return self.pokemons[0]
        if len(self.pokemons) == 2:
            return self.add_recu("", self.pokemons)
        s = self.pokemons[0] + "\n"
        s += "----\n"
        for poke in self.pokemons[1:]:
            s += poke[0] + "\n"
        return s

    def add_recu(self, s, pokemons):
        s += pokemons[0]
        if len(pokemons) == 2:
            s += " -> "
            s = self.add_recu(s, pokemons[1])
        return s
