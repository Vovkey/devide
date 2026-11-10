import math
import pygame

def draw_rectangle(surface, x, y, width, height, color):
    pygame.draw.rect(
        surface,
        color,
        (x, y, width, height)
    )

def draw_triangle(surface, points, color):
    pygame.draw.polygon(surface, color, points)

def draw_triangles(surface, triangles, palette):

    for i, triangle in enumerate(triangles):
        color = palette[i % len(palette)]

        pygame.draw.polygon(
            surface,
            color,
            triangle.points
        )

def draw_line(surface, start, end, color, thickness=2):
    pygame.draw.line(
        surface,
        color,
        start,
        end,
        thickness
    )

def draw_circle(surface, x, y, radius, color):
    pygame.draw.circle(
        surface,
        color,
        (x, y),
        radius
    )

def draw_filled_rectangle(
    surface,
    x, y,
    width, height,
    color,
    padding=3
):
    rect = pygame.Rect(
        x + padding,
        y + padding,
        width - padding * 2,
        height - padding *2
    )

    pygame.draw.rect(surface, color, rect)

def draw_branches(surface, branches, palette):

    for branch in branches:
        color = palette[branch.depth % len(palette)]
        thickness = max(1, branch.depth)

        pygame.draw.line(
            surface,
            color,
            branch.start,
            branch.end,
            thickness
        )
