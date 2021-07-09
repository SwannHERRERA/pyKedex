from model.item import Item

def parse_item(item):
  name = item['name']
  cost = item['cost']
  category = item['category']['name']
  Id = item['id']
  return Item(name, cost, Id, category)