import math
from dataclasses import dataclass

@dataclass
class Branch:
    start: tuple
    end: tuple
    depth: int

def generate_branches(
    start,
    length,
    angle,
    depth,
    angle_spread=0.5,
    length_factor=0.7
):

    branches = []

    def grow(x, y, length, angle, depth):
        if depth <= 0:
            return

        end_x = x + math.cos(angle) * length
        end_y = y + math.sin(angle) * length

        branches.append(
            Branch(
                (x, y),
                (end_x, end_y),
                depth
            )
        )

        new_length = length * length_factor

        grow(
            end_x, end_y,
            new_length,
            angle - angle_spread,
            depth - 1
        )

        grow(
            end_x, end_y,
            new_length,
            angle + angle_spread,
            depth - 1
        )
    grow(
        start[0],
        start[1],
        length,
        angle,
        depth
    )

    return branches
