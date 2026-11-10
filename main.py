import pygame
import settings
from core import renderer
from algorithms.rectangles import divide_rectangle

def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (settings.WIDTH, settings.HEIGHT)
    )

    pygame.display.set_caption(settings.TITLE)

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill(settings.BACKGROUND)

        divide_rectangle(
            screen,
            100, 100,
            1000, 600,
            depth=7
        )

        pygame.display.flip()

        clock.tick(settings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
