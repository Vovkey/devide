import select

import pygame

class Sidebar:

    def __init__(self):
        self.width = 280
        self.background = (30, 30, 40)
        self.text_color = (240, 240, 240)
        self.accent = (110, 160, 255)
        self.input_background = (45, 45, 60)

        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 23)

        self.algorithms = [
            "Rectangles",
            "Triangles",
            "Branching"
        ]

        self.selected_algorithm = 0

        self.seed = "42"
        self.seed_active = False
        self.seed_input = pygame.Rect(20, 340, 240, 40)

        self.generate_button = pygame.Rect(
            20, 650, 240, 50
        )

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.background,
            (0, 0, self.width, screen.get_height())
        )

        title = self.font.render(
            "DEVIDE",
            True,
            self.accent
        )
        screen.blit(title, (20, 25))

        label = self.small_font.render(
            "ALGORITHM",
            True,
            self.accent
        )
        screen.blit(label, (20, 100))

        for i, algorithm in enumerate(self.algorithms):

            rect = pygame.Rect(
                20, 135 + i * 45, 240, 38
            )

            color = (
                self.accent
                if i == self.selected_algorithm
                else (50, 50, 65)
            )

            pygame.draw.rect(
                screen,
                color,
                rect,
                border_radius=6
            )


            text = self.small_font.render(
                algorithm,
                True,
                self.text_color
            )

            screen.blit(
                text,
                (rect.x + 12, rect.y +9)
            )

        seed_label = self.small_font.render(
            "SEED",
            True,
            self.accent
        )
        screen.blit(seed_label, (20, 310))

        input_color = (
            (60, 60, 80)
            if self.seed_active
            else self.input_background
        )

        pygame.draw.rect(
            screen,
            input_color,
            self.seed_input,
            border_radius=6
        )

        pygame.draw.rect(
            screen,
            self.accent if self.seed_active else (80, 80, 100),
            self.seed_input,
            width=2,
            border_radius=6
        )

        seed_text = self.font.render(
            self.seed, True, self.text_color
        )

        screen.blit(seed_text, (self.seed_input.x +10,
                                self.seed_input.y + 7))

        pygame.draw.rect(
            screen,
            self.accent,
            self.generate_button,
            border_radius=8
        )

        button_text = self.small_font.render(
            "GENERATE",
            True,
            (255, 255, 255)
        )

        screen.blit(
            button_text,
            (self.generate_button.x + 75,
             self.generate_button.y + 15)
        )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                self.seed_active = self.seed_input.collidepoint(
                    event.pos
                )

                mouse_x, mouse_y = event.pos

                for i in range(len(self.algorithms)):
                    rect = pygame.Rect(
                        20, 135 + i * 45, 240, 38
                    )

                    if rect.collidepoint(mouse_x, mouse_y):
                        self.selected_algorithm = i

                if self.generate_button.collidepoint(event.pos):
                    return "generate"

        if event.type == pygame.KEYDOWN and self.seed_active:
            if event.key == pygame.K_BACKSPACE:
                self.seed = self.seed[:-1]

            elif event.key == pygame.K_RETURN:
                self.seed_active = False

            elif event.unicode.isdigit() and len(self.seed) < 12:
                self.seed += event.unicode

        return None
