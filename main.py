import pygame
from algorithms import rectangles
import settings
from core import renderer
from algorithms.rectangles import generate_rectangles

palette = [
    (235, 90, 90),
    (245, 170, 90),
    (245, 215, 130),
    (100, 170, 190),
    (100, 120, 180),
    (150, 110, 180)
]

rectangles = generate_rectangles(
    100, 100,
    1000, 600,
    depth=8,
    seed=1223,
    min_size=35,
    stop_chance=0.1
)

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

        for rect in rectangles:
            color = palette[rect.depth % len(palette)]

            renderer.draw_filled_rectangle(
                screen,
                rect.x,
                rect.y,
                rect.width,
                rect.height,
                color,
                padding=3
            )

        pygame.display.flip()

        clock.tick(settings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
