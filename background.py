import pygame
from settings import *


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        background_image = pygame.image.load("image/first_level_testing.png")

        self.image = background_image
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = HEIGHT // 2 - HEIGHT_LEVEL // 2

        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx