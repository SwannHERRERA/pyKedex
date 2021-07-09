class Item:
    def __init__(self, name, cost, Id, category):
        self.name = name
        self.id = Id
        self.cost = cost
        self.category = category

    def __str__(self):
        return f'{self.id} {self.name}: {self.cost}$ categorie: {self.category}'