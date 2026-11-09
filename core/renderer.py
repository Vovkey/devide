import pygame

def draw_rectangle(surface, x, y, width, height, color):
    pygame.draw.rect(
        surface,
        color,
        (x, y, width, height)
    )

def draw_triangle(surface, points, color):
    pygame.draw.polygon(surface, color, points)

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
