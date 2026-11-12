from dataclasses import dataclass
import random

@dataclass
class Triangle:
    points: tuple
    depth: int

def midpoint(a, b, rng, variation):

    t = 0.5 + rng.uniform(-variation, variation)

    return (
        a[0] + (b[0] - a[0]) * t,
        a[1] + (b[1] - a[1]) * t
    )

def generate_triangles(
    points,
    depth,
    rng,
    variation=0.0
):

    triangles = []

    if variation > 0:
        points = list(points)

        side_lengths = [
            ((points[i][0] - points[(i+1) % 3][0]) ** 2 +
             (points[i][1] - points[(i+1) % 3][1]) **2) ** 0.5
            for i in range(3)
        ]

        scale = sum(side_lengths) / 3

        max_offset = scale * variation * 0.15

        randomized_points = []

        for x, y in points:
            new_x = x + rng.uniform(-max_offset, max_offset)
            new_y = y + rng.uniform(-max_offset, max_offset)

            randomized_points.append((new_x, new_y))

        points = randomized_points

    def subdivivde(a, b, c, current_depth):

        if current_depth <= 0:
            triangles.append(
                Triangle((a, b, c), current_depth)
            )
            return

        ab = midpoint(a, b, rng, variation)
        bc = midpoint(b, c, rng, variation)
        ca = midpoint(c, a, rng, variation)

        subdivivde(a, ab, ca, current_depth - 1)
        subdivivde(ab, b, bc, current_depth -1)
        subdivivde(ca, bc, c, current_depth - 1)
        subdivivde(ab, bc, ca, current_depth - 1)

    subdivivde(*points, depth)

    return triangles
