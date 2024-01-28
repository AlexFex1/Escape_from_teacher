import pygame
from settings import *


# Создание сущности за которую будет играть пользователь (игрок)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_image = pygame.image.load("image/player_v1.png")

        self.image = player_image
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT // 2 + HEIGHT_LEVEL // 2 - 26
        self.speedx = 0

        self.isJump = False
        self.jumpCount = 7

    
    def update(self):
        self.rect.x += self.speedx

        if self.isJump is True:
            if self.jumpCount >= -7:
                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 0.5
            else:
                self.isJump = False
                self.jumpCount = 7
