from dataclasses import dataclass

@dataclass
class Triangle:
    points: tuple
    depth: int


def generate_triangles(
    points,
    depth,
    rng,
    variation=0.0
):

    triangles = []
    midpoint_cache = {}

    if variation > 0:
        points = list(points)

        side_lengths = [
            ((points[i][0] - points[(i+1) % 3][0]) ** 2 +
             (points[i][1] - points[(i+1) % 3][1]) **2) ** 0.5
            for i in range(3)
        ]

        scale = sum(side_lengths) / 3

        max_offset = scale * variation * 0.08

        points = [
            (
                x + rng.uniform(-max_offset, max_offset),
                y + rng.uniform(-max_offset, max_offset)
            )
            for x, y in points
        ]

    def midpoint(a, b):
        edge = tuple(sorted((a, b)))

        if edge not in midpoint_cache:
            t = 0.5 + rng.uniform(-variation, variation) * 0.5

            midpoint_cache[edge] = (
                a[0] + (b[0] - a[0]) * t,
                a[1] + (b[1] - a[1]) * t
            )

        return midpoint_cache[edge]

    def subdivivde(a, b, c, current_depth):

        if current_depth <= 0:
            triangles.append(
                Triangle((a, b, c), current_depth)
            )
            return

        ab = midpoint(a, b)
        bc = midpoint(b, c)
        ca = midpoint(c, a)

        subdivivde(a, ab, ca, current_depth - 1)
        subdivivde(ab, b, bc, current_depth -1)
        subdivivde(ca, bc, c, current_depth - 1)
        subdivivde(ab, bc, ca, current_depth - 1)

    subdivivde(*points, depth)

    return triangles
