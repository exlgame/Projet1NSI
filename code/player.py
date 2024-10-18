import pygame
from pygame.display import update

from entity import Entity
from screen import Screen
from keylistener import Keylistener

class Player(Entity):

    def __init__(self, keylistener: Keylistener,screen : Screen, x: int,y: int):
        super().__init__(keylistener,screen,x,y)

        self.pokedollars = 0

    def update(self):
        self.check_move()
        super().update()

    def check_move(self):
        if self.animation_walk is False:
            if self.keylistener.keypressed(pygame.K_q):
                self.move_left()
            elif self.keylistener.keypressed(pygame.K_d):
                self.move_right()
            elif self.keylistener.keypressed(pygame.K_z):
                self.move_up()
            elif self.keylistener.keypressed(pygame.K_s):
                self.move_down()