import pygame
from settings import FPS
from terminate import terminate


def Pause():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)