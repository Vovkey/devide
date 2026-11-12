import pygame
import settings
import math
import random

from core import renderer
from core.randomness import get_rng
from core.generator import generate_art

from algorithms.rectangles import generate_rectangles
from algorithms.triangles import generate_triangles
from algorithms.branching import generate_branches

from ui.sidebar import Sidebar

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

rectangles = generate_art(
    "rectangles",
    settings.SEED,
    x=100,
    y=100,
    width=1000,
    height=600,
    depth=8,
)

triangle_points = (
    (600, 100),
    (200, 650),
    (1000, 650)
)

triangles = generate_art(
    "triangles",
    settings.SEED,
    points=triangle_points,
    depth=5
)

branches = generate_art(
    "branching",
    settings.SEED,
    start=(600, 700),
    length=150,
    angle=-math.pi / 2,
    depth=9,
)

def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (settings.WIDTH, settings.HEIGHT)
    )

    pygame.display.set_caption(settings.TITLE)

    clock = pygame.time.Clock()

    sidebar = Sidebar()
    current_art = []

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            action = sidebar.handle_event(event)
            if sidebar.variation_changed:
                sidebar.variation_changed = False

                if current_art_algorithm == "triangles":
                    current_art = generate_art(
                        "triangles",
                        int(sidebar.seed or "0"),
                        points=(
                            (screen.get_width() // 2, 80),
                            (330, screen.get_height() - 80),
                            (screen.get_width() - 40, screen.get_height() - 80)
                        ),
                        depth=5,
                        variation=sidebar.variation
                    )

            if action == "generate":

                algorithm = sidebar.algorithms[
                    sidebar.selected_algorithm
                ].lower()

                seed = int(sidebar.seed or 0)

                if algorithm == "rectangles":
                    current_art = generate_art(
                        algorithm,
                        seed,
                        x=320,
                        y=100,
                        width=800,
                        height=600,
                        depth=8
                    )

                elif algorithm == "triangles":
                    current_art = generate_art(
                        algorithm,
                        seed,
                        points=((720, 100), (370, 650), (1070, 650)),
                        depth=5,
                        variation=sidebar.variation
                    )

                elif algorithm == "branching":
                    current_art = generate_art(
                        algorithm,
                        seed,
                        start=(720, 700),
                        length=150,
                        angle=-math.pi / 2,
                        depth=9
                    )

                current_art_algorithm = algorithm

        screen.fill(settings.BACKGROUND)

        if current_art and current_art_algorithm == "rectangles":
                for rect in current_art:
                    color = settings.ACCENT
                    renderer.draw_filled_rectangle(
                        screen,
                        rect.x,
                        rect.y,
                        rect.width,
                        rect.height,
                        color,
                        padding=3
                    )

        elif current_art and current_art_algorithm == "triangles":
                renderer.draw_triangles(
                    screen,
                    current_art,
                    [settings.ACCENT, (235, 90, 90), (245, 170, 90)]
                )

        elif current_art and current_art_algorithm == "branching":
                renderer.draw_branches(
                    screen,
                    current_art,
                    [settings.ACCENT, (235, 90, 90), (245, 170, 90)]
                )


        sidebar.draw(screen)

        pygame.display.flip()

        clock.tick(settings.FPS)

    pygame.quit()



if __name__ == "__main__":
    main()
