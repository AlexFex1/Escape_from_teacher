import pygame

from settings import *

from Player import Player
from background import Background
from pufik import Pufik
from table import Table
from desk import Desk

# from terminate import terminate

from start_scree_window import start_screen
from pause import Pause

def stop_back_objects():
    for obj in back_objects:
        obj.speedx = 0

def move_back_objects(dx):
    for obj in back_objects:
        obj.speedx = dx

def objects_dx():
    player.speedx = 0
    stop_back_objects()

    keystate = pygame.key.get_pressed()
    if not pygame.sprite.collide_mask(player, pufik1) and not pygame.sprite.collide_mask(player, pufik2) and not pygame.sprite.collide_mask(player, pufik3) and not pygame.sprite.collide_mask(player, table1) and not pygame.sprite.collide_mask(player, table2):
        if keystate[pygame.K_LEFT] and player.rect.left != 20:
            #print('left')
            if player.rect.left < 500 and background.rect.left != 0:
                if background.rect.left > -8:
                    move_back_objects(-background.rect.left)
                else:
                    move_back_objects(8)
                #print('back')
            else:
                player.speedx = -8
                #print('pl')

        if keystate[pygame.K_RIGHT] and player.rect.right != WIDTH - 20:
            #print('right')
            if player.rect.right > WIDTH - 500 and background.rect.right > WIDTH + 8:
                if background.rect.right < WIDTH + 8:
                    move_back_objects(WIDTH - background.rect.right)
                else:
                    move_back_objects(-8)
                #print('back')
            else:

                player.speedx = 8
                #print('pl')

        if keystate[pygame.K_SPACE]:
            player.isJump = True
    else:
        player.rect.centerx = 100
        # player.rect.bottom = HEIGHT // 2 + HEIGHT_LEVEL // 2 - 26

        background.rect.left = 0

        pufik1.rect.x = 596
        pufik2.rect.x = 1980
        pufik3.rect.x = 3396

        table1.rect.x = 1284
        table2.rect.x = 2696

        desk.rect.x = 2568


if __name__ == "__main__":
    # Инициальзация игры
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Game")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    back_objects = pygame.sprite.Group()
    obstacle_objects = pygame.sprite.Group()

    player = Player()
    background = Background()

    pufik1 = Pufik(596)
    pufik2 = Pufik(1980)
    pufik3 = Pufik(3396)

    table1 = Table(1284)
    table2 = Table(2696)

    desk = Desk(2568, 212)

    for item in pufik1, pufik2, pufik3, table1, table2:
        obstacle_objects.add(item)

    for item in background, pufik1, pufik2, pufik3, table1, table2, desk:
        back_objects.add(item)

    for item in background, pufik1, pufik2, pufik3, table1, table2, desk, player:
        all_sprites.add(item)
    

    # background_image = pygame.image.load("image/first_level.png")

    start_screen(screen)  # начальное окно

    # Цикл игры
    # так как в игре используется пауза, то переменной для закрытия и выключения while не нада
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
