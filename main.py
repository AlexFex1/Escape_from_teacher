import pygame
# Импорт Частей игры
from settings import *

from Player import Player
from background import Background

# from terminate import terminate

from start_scree_window import start_screen
from pause import Pause


def objects_dx():
    player.speedx = 0
    background.speedx = 0

    keystate = pygame.key.get_pressed()
    
    if keystate[pygame.K_LEFT]:
        if player.rect.left < 50 and background.rect.x != 0:
            background.speedx = 8
        else:
            player.speedx = -8

    if keystate[pygame.K_RIGHT]:
        if player.rect.right > WIDTH - 50 and background.rect.x != WIDTH:
            background.speedx = -8
        else:
            player.speedx = 8

    if keystate[pygame.K_SPACE]:
        player.isJump = True


if __name__ == "__main__":
    # Инициальзация игры
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Game")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    player = Player()
    background = Background()
    
    all_sprites.add(background)
    all_sprites.add(player)
    

    # background_image = pygame.image.load("image/first_level.png")

    start_screen()  # начальное окно

    # Цикл игры
    # running = True
    while True:
        clock.tick(FPS) # Контроль ФПС

        for event in pygame.event.get(): # Ввод событий
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # Пауза
                Pause()

        objects_dx()
        all_sprites.update()

        screen.fill((26, 72, 118))
        # screen.blit(background.image, background.rect)
        all_sprites.draw(screen)

        pygame.display.flip()
