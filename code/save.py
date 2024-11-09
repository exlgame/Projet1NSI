import json
import datetime
import pathlib

from pygame.examples.multiplayer_joystick import player

from map import Map
from player import Player
from sql import SQL

class Save:
    def __init__(self, path:str, map: Map):
        self.path = path
        self.map = map
        self.sql = SQL()

    def save(self):
        self.map.save_in_file(self.path)
        positon = self.map.player.position
        player_info = self.map.player.position
        player_info = {
            "name": self.map.player.direction,
            #"type": self.map.player.type,
            "position": {
                "x": positon[0],
                "y": positon[1]
            },
            "pokemon": self.map.player.pokemons,
            "inventory": self.map.player.inventory,
            "pokedex": self.map.player.pokedex,
            "pokedollars": self.map.player.pokedollars,
            "ingame_time": self.map.player.ingame_time.seconds,
        }
        map_info = {
            "path": self.map.current_map.name,
            "map_name": self.map.current_map.name
        }
        data = {
            "player": player_info,
            "map": map_info
        }

        with open(f"../assets/{self.path}/data", "w") as file:
            file.write(self.dump(data))

    def load(self):
        if pathlib.Path(f"../assets/{self.path}/data").exists():
            with open(f"../assets/{self.path}/data", "r") as file:
                data = json.load(file)
            self.map.path_name = data["map"]["name"]
            self.map.current_map = data["map"]["map_name"]
            self.map.player = Player(self.map.screen, self.map.controller, data["player"]["name"],
                                     data["player"]["position"]["x"], data["player"]["position"]["y"],
                                     datetime.timedelta(seconds=data["player"]["ingame_time"]))
            self.map.player.direction = data["player"]["direction"]
            self.map.player.pokemons = data["player"]["pokemon"]
            self.map.player.inventory = data["player"]["inventory"]
            self.map.player.pokedex = data["player"]["pokedex"]
            self.map.player.pokedollars = data["player"]["pokedollars"]

    def dump(self, element: dict):
        return json.dumps(element, indent=4)