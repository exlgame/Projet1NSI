import json
import datetime
import pathlib

from map import Map
from player import Player
from sql import SQL

class Save:
    def __init__(self, path: str, map: Map):
        self.path = path
        self.map = map
        self.sql = SQL()

    def save(self):
        self.map.save_in_file(self.path)
        position = self.map.player.position
        player_info = {
            "name": self.map.player.name,
            "type": self.map.player.type,
            "position": {
                "x": position[0],
                "y": position[1]
            },
            "direction": self.map.player.direction,
            "pokemon": self.map.player.pokemon,
            "inventory": self.map.player.inventory,
            "pokedex": self.map.player.pokedex,
            "pokedollars": self.map.player.pokedollars,
            "ingame_time": self.map.player.ingame_time.seconds,
        }