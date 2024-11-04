import json

import pygame
import pytmx
import pyscroll

from player import Player
from screen import Screen
from switch import Switch


class Map:

    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None
        self.player: Player | None = None
        self.switchs: list[Switch] | None = None

        self.current_map: Switch = Switch("switch", "map_0", pygame.Rect(0, 0, 0, 0), 0)

        self.switch_map(self.current_map)

    def switch_map(self, switch: Switch) -> None:
        self.tmx_data = pytmx.load_pygame(f"../assets/map/{switch.name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

        for obj in self.tmx_data.objects:
            type = obj.name.split(" ")[0]
            if type == "switch":
                self.switchs.append(Switch(
                    type, obj.name.split(" ")[1], pygame.Rect(obj.x, obj.y, obj.width, obj.height),
                    int(obj.name.split(" ")[-1])
                ))

    def add_player(self, player) -> None:
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()
        self.player.add_switchs(self.switchs)

    def update(self) -> None:
        if self.player:
            if self.player.change_map:
                self.switch_map(self.player.change_map)
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())

    def save_in_file(self, path: str):
        if not pathlib.Path(f"../assets/saves/{path}/maps/{self.current_map.name}").exists():
            os.makedirs(f"../assets/saves/{path}/maps/{self.current_map.name}")
        with open(f"../assets/saves/{path}/maps/{self.current_map.name}", "w") as file:
            json.dump(self.tmx_data.tiledgdimap, file)
        for i, layer in enumerate(self.tmx_data.visible_layers):
            with open(f"../assets/saves/{path}/maps/{self.current_map.name}/layer{i}", "w") as file:
                json.dump(layer.data, file)
