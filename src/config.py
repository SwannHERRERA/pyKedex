class Config:
    def __init__(self, base_url, image_path):
        self.base_url = base_url
        self.image_path = image_path


config = Config("https://pokeapi.co/api/v2", "image.txt")


class PokeStat:
    SPEED = "speed"
    HP = "hp"
    ATTACK = "attack"
    WEIGHT = "weight"
