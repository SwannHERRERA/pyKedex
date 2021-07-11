import sys
import requests
from PIL import Image
import webbrowser


class ImgTransformer:
    ascii_char = list(
        "@M%WXmBU&ZQ$dpOLwh8kYCn#bqaxJoIuf0}(])[{tz|/jvc\\?l+*ri<1>!^~_\";-,`:'. "
    )

    def __init__(self, img_url, output_file=config.img_path, char_list=None):
        self.img_url = img_url
        self.output_file = output_file
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
        # lower is ascii_factor = better detail
        ascii_factor = 20
        self.resize(width, height)
        self.grayfy()
        pixels = self.img.getdata()
        characters = "".join(
            [self.ascii_char[pixel // ascii_factor] for pixel in pixels]
        )
        pixel_count = len(characters)
        ascii_image = "\n".join(
            characters[i : (i + height)] for i in range(0, pixel_count, height)
        )
        return ascii_image

    def save_to_file(self):
        ascii_image = self.pixels_to_ascii()
        with open(self.output_file, "w") as f:
            f.write(ascii_image)
