import pygame
from settings import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visivle_sprites = pygame. sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row in WORLD_MAP:
            print(row)

    def run(self):
        pass #TBA
