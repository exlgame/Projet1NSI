import json
import pygame
import datetime

from controller import Controller
from map import Map
from player import Player
from screen import Screen
from sql import SQL
from save import Save
from tool import Tool


class Option:

    def __init__(self, screen: Screen, controller: Controller, map: Map, language: str, save: Save):
        self.screen = screen
        self.controller = controller
        self.map = map
        self.language = language
        self.save = save
        self.sql = SQL()
        self.player = self.map.player

        self.full_background: pygame.Surface = pygame.surface.Surface(self.screen.get_size())
        self.image_background: pygame.Surface | None = None
        self.initialization = bool = False

    def update(self):
        if not self.initialization:
            self.initialization = True
            self.initialize()
        self.draw()

    def initialize (self):
        self.image_background = self.screen.image_screen()
        self.image_background = Tool.blur(self.image_background, 2)

    def draw(self):
        self.player.update_ingame_time()
        self.full_background.blit(self.image_background, (0, 0))