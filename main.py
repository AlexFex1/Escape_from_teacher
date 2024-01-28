import pygame
# Импорт Частей игры
from settings import *

from Player import Player
from background import Background
from pufik import Pufik

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
    
    if keystate[pygame.K_LEFT]:
        #print('left')
        if player.rect.left < 20:
            if background.rect.left > -8:
                move_back_objects(-background.rect.left)
            else:
                move_back_objects(8)
            #print('back')
        else:
            player.speedx = -8
            #print('pl')

    if keystate[pygame.K_RIGHT]:
        #print('right')
        if player.rect.right > WIDTH - 20:
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


if __name__ == "__main__":
    # Инициальзация игры
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Game")

    clock = pygame.time.Clock()
    pufik = Pufik()

    all_sprites = pygame.sprite.Group()
    back_objects = pygame.sprite.Group()
    obstacle_objects = pygame.sprite.Group()

    player = Player()
    background = Background()
    obstacle_objects.add(pufik)
    back_objects.add(background)
    back_objects.add(pufik)
    all_sprites.add(background)
    all_sprites.add(pufik)
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
