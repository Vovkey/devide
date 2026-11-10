import random
from core.renderer import draw_filled_rectangle
from dataclasses import dataclass

from settings import HEIGHT

@dataclass
class Rectangle:
    x: float
    y: float
    width: float
    height: float
    depth: int

def generate_rectangles(
    x, y,
    width, height,
    depth,
    seed=None,
    min_size=35,
    stop_chance=0.15
):
    rng = random.Random(seed)
    rectangles = []

    def divide(x, y, width, height, depth):

        if depth <= 0:
            rectangles.append(
                Rectangle(x, y, width, height, depth)
            )
            return

        if width < min_size * 2 or height < min_size * 2:
            rectangles.append(
                Rectangle(x, y, width, height, depth)
            )
            return

        if rng.random() < stop_chance:
            rectangles.append(
                Rectangle(x, y, width, height, depth)
            )
            return

        vertical = rng.choice([True, False])

        if vertical:
            split = rng.uniform(0.35, 0.65) * width

            divide(x, y, split, height, depth -1)
            divide(
                x + split, y,
                width - split, height,
                depth -1
            )

        else:
            split = rng.uniform(0.35, 0.65) * height

            divide(x, y, width, split, depth -1)
            divide(
                x, y + split,
                width,height - split,
                depth -1
            )

    divide(x, y, width, height, depth)
    return rectangles
