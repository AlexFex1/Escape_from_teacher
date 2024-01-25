import pygame
# Импорт Частей игры
from settings import WIDTH, HEIGHT, FPS

from Player import Player
#from background import Background

from terminate import terminate

from start_scree_window import start_screen


if __name__ == "__main__":
    # Инициальзация игры
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Game")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    player = Player()
    #background = Background()
    
    all_sprites.add(player)

    background_image = pygame.image.load("image/first_level.png")

    start_screen()

    # Цикл игры
    # running = True
    while True:
        clock.tick(FPS) # Контроль ФПС

        for event in pygame.event.get(): # Ввод событий
            if event.type == pygame.QUIT: # Выключение
                terminate()

        all_sprites.update()

        screen.fill((255, 255, 255))
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
