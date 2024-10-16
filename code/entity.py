import pygame
from tool import Tool
from keylistener import Keylistener


class Entity(pygame.sprite.Sprite):

    def __init__(self, keylistener: Keylistener):
        super().__init__()
        self.keylistener = keylistener
        self.spritesheet= pygame.image.load("../assets/sprite/hero_01_red_m_walk.png")
        self.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position = [0,0]
        self.rect: pygame.Rect = pygame.Rect (0, 0 ,16 ,32)

    def update(self):
        self.check_move()
        self.rect.topleft = self.position

    def move_left(self):
        self.position[0] -= 1

    def move_right(self):
        self.position [0] += 1

    def move_up(self):
        self.position[1] -= 1

    def move_down(self):
        self.position[1] +=1