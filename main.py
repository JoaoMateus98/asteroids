import pygame
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((1980, 1020))
    clock = pygame.time.Clock()
    running = True

    player = Player(screen=screen, size=25)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        # update screen here

        player.draw_player()

        draw_grid(screen)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


def draw_grid(screen: pygame.Surface):
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    screen_horizontal_center = screen.get_width() / 2
    screen_vertical_center = screen.get_height() / 2

    pygame.draw.line(screen, "white", (screen_horizontal_center, 0),
                     (screen_horizontal_center, screen_height), 1)
    pygame.draw.line(screen, "white", (0, screen_vertical_center),
                     (screen_width, screen_vertical_center), 1)


if __name__ == '__main__':
    main()
