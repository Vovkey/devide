import pygame
import settings
from core import renderer

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

        renderer.draw_rectangle(
            screen,
            100, 100,
            1000, 600,
            settings.CANVAS_BACKGROUND
        )

        renderer.draw_rectangle(
            screen, 200, 200, 200, 150,
            (255, 100, 100)
        )

        renderer.draw_triangle(
            screen,
            [(600, 200), (500, 400), (700, 400)],
            (100,200,255)
        )

        renderer.draw_circle(
            screen, 900, 300, 75,
            (150, 255, 150)
        )

        renderer.draw_line(
            screen,
            (200,500),
            (1000, 500),
            settings.WHITE,
            3
        )

        pygame.display.flip()

        clock.tick(settings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
