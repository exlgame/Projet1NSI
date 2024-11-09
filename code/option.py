import json
import pygame
import datetime

from controller import Controller
from map import Map
from player import Player
from screen import Screen
from sql import SQL
from save import Save


class Option:

    def __init__(self, screen: Screen, controller: Controller, map: Map, language: str, save: Save):
        self.screen = screen
        self.controller = controller
        self.map = map
        self.language = language
        self.save = save
