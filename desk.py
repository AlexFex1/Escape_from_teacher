import pygame
from settings import *


class Desk(pygame.sprite.Sprite):
    def __init__(self, x, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image/dask.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y + HEIGHT // 2 - HEIGHT_LEVEL // 2

        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_f]:
            self.image = pygame.image.load("image/dask_f.png")
