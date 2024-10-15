import pygame


class Screen:
    def __int__(self):
        self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.framerate = 60

def update(self):
    pygame.display.flip()
    pygame.display.update()
    self.clock.tick(self.framerate)
    self.display.fill((0, 0, 0))