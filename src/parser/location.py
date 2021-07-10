from model.location import Location


def parse_location(location):
    name = location["name"]
    region_name = location["region"]["name"]
    areas = [area["name"] for area in location["areas"]]
    return Location(name, region_name, areas)
