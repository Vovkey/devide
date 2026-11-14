import select

import pygame

import settings

import algorithms

class Sidebar:

    def update_variation(self, mouse_x):
        mouse_x = max(
            self.slider_track.left,
            min(mouse_x, self.slider_track.right)
        )

        self.slider_handle_x = mouse_x

        new_variation = (
            (mouse_x - self.slider_track.left)
            / self.slider_track.width
        ) * 0.4

        if round(new_variation, 3) != round(self.variation, 3):
            self.variation = new_variation
            self.variation_changed = True

    def __init__(self):
        self.width = 280
        self.background = (30, 30, 40)
        self.text_color = (240, 240, 240)
        self.accent = (110, 160, 255)
        self.input_background = (45, 45, 60)

        self.variation = 0.15
        self.slider_dragging = False

        self.slider_track = pygame.Rect(20, 440, 240, 8)
        self.slider_handle_x = 20 + int(
            (self.variation / 0.4) * 240
        )

        self.variation_changed = False

        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 23)

        self.algorithms = [
            "Rectangles",
            "Triangles",
            "Branching"
        ]

        self.selected_algorithms = {"rectangles"}

        self.seed = "42"
        self.seed_active = False
        self.seed_input = pygame.Rect(20, 340, 240, 40)

        self.generate_button = pygame.Rect(
            20, 650, 240, 50
        )

        self.palette_names = [
            "Ocean",
            "Sunset",
            "Forest",
            "Neon",
            "Monochrome"
        ]
        self.selected_palette = 0
        self.palette_button = pygame.Rect(10, 530, 240, 45)
        self.palette_last_click = -500

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

            selected = algorithm.lower() in self.selected_algorithms

            if selected :
                color = settings.ACCENT

            else:
                color = (45, 45, 55)

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

        variation_label = self.small_font.render(
            "TRIANGLE VARIATION", True, self.accent
        )
        screen.blit(variation_label, (20, 405))

        value_text = self.small_font.render(
            f"{self.variation: .2f}", True, self.text_color
        )
        screen.blit(value_text, (210, 405))

        pygame.draw.rect(
            screen,
            (70, 70, 85),
            self.slider_track,
            border_radius=4
        )

        progress_width = self.slider_handle_x - self.slider_track.x

        pygame.draw.rect(
            screen,
            self.accent,
            (self.slider_track.x, self.slider_track.y,
             progress_width, self.slider_track.height),
            border_radius=4
        )

        pygame.draw.circle(
            screen,
            self.accent,
            (self.slider_handle_x, self.slider_track.centery),
            9
        )

        label = self.font.render(
            "COLOR PALETTE",
            True,
            settings.ACCENT
        )

        screen.blit(label, (10, 495))

        pygame.draw.rect(
            screen,
            (45, 45, 55),
            self.palette_button,
            border_radius=8
        )

        pygame.draw.rect(
            screen,
            settings.ACCENT,
            self.palette_button,
            2,
            border_radius=8
        )

        palette_name = self.palette_names[self.selected_palette]

        text = self.font.render(
            f"  {palette_name}  ",
            True,
            settings.WHITE
        )

        text_rect = text.get_rect(
            center=self.palette_button.center
        )

        screen.blit(text, text_rect)


    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                self.seed_active = self.seed_input.collidepoint(
                    event.pos
                )

                mouse_x, mouse_y = event.pos

                for i, name in enumerate(self.algorithms):
                    rect = pygame.Rect(
                        20, 135 + i * 45, 240, 38
                    )

                    if rect.collidepoint(event.pos):
                        algorithm = name.lower()

                        if algorithm in self.selected_algorithms:
                            self.selected_algorithms.remove(algorithm)
                        else:
                            self.selected_algorithms.add(algorithm)

                if self.slider_track.inflate(0, 25).collidepoint(event.pos):
                    self.slider_dragging = True

                    self.update_variation(event.pos[0])

                if self.generate_button.collidepoint(event.pos):
                    return "generate"

                if self.palette_button.collidepoint(event.pos):
                    current_time = pygame.time.get_ticks()

                    if current_time - self.palette_last_click >= 500:
                        self.selected_palette = (
                            self.selected_palette + 1
                        ) % len(self.palette_names)

                        self.palette_last_click = current_time

        if event.type == pygame.KEYDOWN and self.seed_active:
            if event.key == pygame.K_BACKSPACE:
                self.seed = self.seed[:-1]

            elif event.key == pygame.K_RETURN:
                self.seed_active = False

            elif event.unicode.isdigit() and len(self.seed) < 12:
                self.seed += event.unicode

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.slider_dragging = False

        if event.type == pygame.MOUSEMOTION:
           if self.slider_dragging:
               self.update_variation(event.pos[0])

        return None
