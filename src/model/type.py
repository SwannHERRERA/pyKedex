import typer

class Type:
    def __init__(self, name, generation, damage_relation, pokemons, moves):
        self.name = name
        self.generation = generation
        self.damage_relation = damage_relation
        self.pokemons = pokemons
        self.moves = moves
    
    def __str__(self):
        type_string = f'{self.name}: from {self.generation}\n'
        type_string += '\n'
        type_string += self.getPokemons()
        type_string += '\n'
        type_string += self.getMoves()
        type_string += '\n'
        type_string += self.getTypeChart()
        return type_string

    def getWeaknessAndStrength(self):
        return ''

    def getPokemons(self):
        pokemons = 'pokemons: [ '
        for name in self.pokemons:
            pokemons += f'{name} '
        pokemons += ']\n'
        return pokemons

    def getMoves(self):
        moves = 'moves: [ ' 
        for name in self.moves:
            moves += f'{name} '
        moves += ']\n'
        return moves
    
    def getTypeChart(self):
        type_chart = ''
        x2to = 'x2to: '
        x2from = 'x2from: '
        div2to = '/2to: '
        div2from = '/2from: '
        x0to = 'x0to: '
        x0form = 'x0form: '
        for typ in self.damage_relation['x2to']:
            x2to += f'{typ} '
        for typ in self.damage_relation['x2from']:
            x2from += f'{typ} '
        for typ in self.damage_relation['/2to']:
            div2to += f'{typ} '
        for typ in self.damage_relation['/2from']:
            div2from += f'{typ} '
        for typ in self.damage_relation['x0to']:
            x0to += f'{typ} '
        for typ in self.damage_relation['x0form']:
            x0form += f'{typ} '
        
        type_chart += typer.style(x2to + '\n', fg=typer.colors.GREEN)
        type_chart += typer.style(x2from + '\n', fg=typer.colors.RED)
        type_chart += typer.style(div2to + '\n', fg=typer.colors.MAGENTA)
        type_chart += typer.style(div2from + '\n', fg=typer.colors.CYAN)
        type_chart += typer.style(x0to + '\n', fg=typer.colors.RED)
        type_chart += typer.style(x0form + '\n', fg=typer.colors.GREEN)
        return type_chart