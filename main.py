import pygame
import settings
import math
import random

from core import renderer
from core.randomness import get_rng
from core.generator import generate_art
from core.palettes import PALETTES

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
    current_art = {}

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            action = sidebar.handle_event(event)
            if sidebar.variation_changed:
                sidebar.variation_changed = False

                if "triangles" in current_art:
                    current_art["triangles"] = generate_art(
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
                seed = int(sidebar.seed or 0)

                current_art = {}

                if "rectangles" in sidebar.selected_algorithms:
                    current_art["rectangles"] = generate_art(
                        "rectangles",
                        seed,
                        x=310,
                        y=50,
                        width=screen.get_width() - 350,
                        height=screen.get_height() - 100,
                        depth=8
                    )

                if "triangles" in sidebar.selected_algorithms:
                    current_art["triangles"] = generate_art(
                        "triangles",
                        seed,
                        points=(
                            (screen.get_width() // 2, 80),
                            (330, screen.get_height() - 80),
                            (screen.get_width() - 40, screen.get_height() - 80)
                        ),
                        depth=5,
                        variation=sidebar.variation
                    )

                if "branching" in sidebar.selected_algorithms:
                    current_art["branching"] = generate_art(
                        "branching",
                        seed,
                        start=(screen.get_width() // 2, screen.get_height() - 50),
                        length=150,
                        angle=-math.pi / 2,
                        depth=9
                    )


        screen.fill(settings.BACKGROUND)

        palette_name = sidebar.palette_names[sidebar.selected_palette]
        colors = PALETTES[palette_name]

        if "rectangles" in current_art:
                for rect in current_art["rectangles"]:
                    renderer.draw_filled_rectangle(
                        screen,
                        rect.x,
                        rect.y,
                        rect.width,
                        rect.height,
                        colors["rectangles"][0],
                        padding=3
                    )

        if "triangles" in current_art:
                renderer.draw_triangles(
                    screen,
                    current_art["triangles"],
                    colors["triangles"]
                )

        if "branching" in current_art:
                renderer.draw_branches(
                    screen,
                    current_art["branching"],
                    colors["branching"]
                )


        sidebar.draw(screen)

        pygame.display.flip()

        clock.tick(settings.FPS)

    pygame.quit()



if __name__ == "__main__":
    main()
