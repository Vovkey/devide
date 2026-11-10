from dataclasses import dataclass

@dataclass
class Triangle:
    points: tuple
    depth: int

def midpoint(a, b):
    return (
        (a[0] + b[0]) / 2,
        (a[1] + b[1]) / 2
    )

def generate_triangles(points, depth):

    triangles = []

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
