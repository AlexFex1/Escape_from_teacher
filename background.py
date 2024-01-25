from typing import Any
import pygame
import os


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        background_image = pygame.image.load("image/first_level.png")

        self.image = background_image
        self.rect = self.image.get_rect

        

    def update(self):
        pass