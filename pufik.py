import pygame
from settings import *


class Pufik(pygame.sprite.Sprite):
    def __init__(self, x: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image/obstacle1.png")
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = x
        self.rect.y = 420 + HEIGHT // 2 - HEIGHT_LEVEL // 2

        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx