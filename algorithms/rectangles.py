import random
from core.renderer import draw_filled_rectangle

def divide_rectangle(
    surface,
    x, y,
    width, height,
    depth,
    min_size=20
):
    if depth <= 0:
        return

    if width < min_size or height < min_size:
        return

    vertical = random.choice([True, False])

    if vertical:

        split = random.uniform(0.35, 0.65) * width

        first_width = split
        second_width = width - split

        first = (x, y, first_width, height)
        second = (x + split, y, second_width, height)

    else:

        split = random.uniform(0.35, 0.65) * height

        first_height = split
        second_height = height - split

        first = (x, y, width, first_height)
        second = (x, y + split, width, second_height)

    colors = [
        (240, 100, 100),
        (100, 100 ,240),
        (240, 200, 100),
        (150, 220, 160)
    ]

    draw_filled_rectangle(
        surface,
        x, y,
        width, height,
        random.choice(colors)
    )

    divide_rectangle(
        surface, *first, depth - 1, min_size
    )

    divide_rectangle(
        surface, *second, depth - 1, min_size
    )
