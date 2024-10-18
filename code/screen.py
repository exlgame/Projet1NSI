import pygame


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Pokemon")
        self.clock = pygame.time.Clock()
        self.framerate = 144
        self.delta_time:float = 0.0

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.display.fill((0, 0, 0))
        self.delta_time = self.clock.get_time()

    def get_delta_time(self):
        return self.delta_time

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
        return self.display