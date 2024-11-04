import pygame


class Switch:

    def __init__(self, type: str, name: str, hitbox: pygame.Rect, port: int):
        self.port = port
        self.name = name
        self.hitbox = hitbox
        self.type = type
