class Item:
    def __init__(self, name, cost, Id, category):
        self.name = name
        self.id = Id
        self.cost = cost
        self.category = category

    def __str__(self):
        return f"""
id: {self.id}
name: {self.name}
price: {self.cost}$
categorie: {self.category}
"""
