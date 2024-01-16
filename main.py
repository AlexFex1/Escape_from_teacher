import pygame
# Импорт Частей игры
from settings import WIDTH, HEIGHT, FPS
from Player import Player


if __name__ == "__main__":
    # Инициальзация игры
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Game")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    # Цикл игры
    running = True
    while running:
        clock.tick(FPS) # Контроль ФПС

        for event in pygame.event.get(): # Ввод событий
            if event.type == pygame.QUIT: # Выключение
                running = False

        all_sprites.update()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
