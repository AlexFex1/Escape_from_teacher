import pygame
from settings import WIDTH, HEIGHT

# Создание сущности за которую будет играть пользователь (игрок)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("YELLOW")
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 2, HEIGHT / 2)
