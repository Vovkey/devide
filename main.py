import pygame
import settings
import math
import random

from core import renderer
from core.randomness import get_rng

from algorithms.rectangles import generate_rectangles
from algorithms.triangles import generate_triangles
from algorithms.branching import generate_branches

rectangle_rng = get_rng(settings.SEED, "rectangles")
triangle_rng = get_rng(settings.SEED, "triangles")
branching_rng = get_rng(settings.SEED, "branch")

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
    rng=branching_rng,
    min_size=35,
    stop_chance=0.1
)

triangle_points = (
    (600, 100),
    (200, 650),
    (1000, 650)
)

triangles = generate_triangles(
    triangle_points,
    depth=5
)

branches = generate_branches(
    start=(600, 700),
    length=15,
    angle=-math.pi / 2,
    depth=9,
    angle_spread=0.5,
    length_factor=1.0,
    rng=branching_rng
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

        renderer.draw_triangles(
            screen,
            triangles,
            palette
        )

        renderer.draw_branches(
            screen,
            branches,
            palette
        )

        pygame.display.flip()

        clock.tick(settings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
