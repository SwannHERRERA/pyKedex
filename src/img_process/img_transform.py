import sys
import requests
from PIL import Image


class ImgTransformer:
    ascii_char = list(
        "@M%WXmBU&ZQ$dpOLwh8kYCn#bqaxJoIuf0}(])[{tz|/jvc\\?l+*ri<1>!^~_\";-,`:'. "
    )

    def __init__(self, img_url, char_list=None):
        self.img_url = img_url
        self.load_img_from_url()
        if char_list is not None:
            self.char_list = char_list

    def load_img_from_url(self):
        try:
            self.img = Image.open(requests.get(self.img_url, stream=True).raw)
        except IOError:
            sys.exit(1)

    def resize(self, width: int, height: int):
        self.img = self.img.resize((width, height))

    def grayfy(self):
        self.img = self.img.convert("L")

    def pixels_to_ascii(self):
        width, height = 100, 100
        ascii_factor = 80  # TODO find a good name
        print(height)
        self.resize(width, height)
        self.grayfy()
        pixels = self.img.getdata()
        characters = "".join(
            [self.ascii_char[pixel // ascii_factor] for pixel in pixels]
        )
        return characters
