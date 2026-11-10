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
    rng,
    angle_spread=0.5,
    length_factor=0.7,
    angle_jitter=0.08,
    length_jitter=0.8,
):

    branches = []

    def grow(x, y, current_length, current_angle, current_depth):
        if current_depth <= 0:
            return

        end_x = x + math.cos(current_angle) * current_length
        end_y = y + math.sin(current_angle) * current_length

        branches.append(
            Branch(
                (x, y),
                (end_x, end_y),
                current_depth
            )
        )

        new_length = (current_length * length_factor * rng.uniform(1 - length_jitter, 1 + length_jitter))

        left_angle = (
            current_angle - angle_spread
            + rng.uniform(-angle_jitter, angle_jitter)
        )

        right_angle = (
            current_angle + angle_spread
            + rng.uniform(-angle_jitter, angle_jitter)
        )

        grow(
            end_x, end_y,
            new_length,
            left_angle,
            current_depth - 1
        )

        grow(
            end_x, end_y,
            new_length,
            right_angle,
            current_depth - 1
        )
    grow(
        start[0],
        start[1],
        length,
        angle,
        depth
    )

    return branches
