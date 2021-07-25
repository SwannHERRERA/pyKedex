from model.evolution_chain import EvolutionChain


def push_childs(evolutions, pokemons):
    for evolve in evolutions:
        poke = [evolve["species"]["name"]]
        pokemons.append(poke)
        if "evolves_to" in evolve:
            push_childs(evolve["evolves_to"], poke)


def parse_evolve(json):
    pokemons = []
    chain = json["chain"]
    pokemons.append(chain["species"]["name"])
    evolutions = chain["evolves_to"]
    push_childs(evolutions, pokemons)
    return EvolutionChain(pokemons)
