from algorithms.rectangles import generate_rectangles
from algorithms.triangles import generate_triangles
from algorithms.branching import generate_branches

from core.randomness import get_rng


def generate_art(algorithm, seed, **params):

    if algorithm == "rectangles":
        rng = get_rng(seed, "rectangles")
        return generate_rectangles(
            **params,
            rng=rng
        )

    elif algorithm == "triangles":
        return generate_triangles(**params)

    elif algorithm == "branching":
        rng = get_rng(seed, "branching")
        return generate_branches(
            **params,
            rng=rng
        )

    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
