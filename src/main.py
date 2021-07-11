from config import Config

import webbrowser


import typer

app = typer.Typer()
config = Config("https://pokeapi.co/api/v2", "image.txt")


@app.command()
def get_pokemons():
    # res = requests.get(config.baseUrl + "/pokemon")
    # pokes = res.json()
    # print(pokes["count"])
    # print(pokes["results"][5]["name"])


if __name__ == "__main__":
    app()
