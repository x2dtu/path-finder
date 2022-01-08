import pygame
import sys
from spot import RED, GREEN, BLUE


class Menu:
    def __init__(self, window, clock):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.clock = clock
        self.circle_cache = {}

    def run(self, is_diagonal):
        while True:
            self.clock()
            mouse = pygame.mouse.get_pos()
            a_star, bfs, dfs, diagonal = self._draw(mouse, is_diagonal)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sleep = 250
                    if self._mouse_over_button(mouse, a_star):
                        pygame.time.wait(sleep)
                        return is_diagonal, False, False
                    if self._mouse_over_button(mouse, bfs):
                        pygame.time.wait(sleep)
                        return is_diagonal, True, False
                    if self._mouse_over_button(mouse, dfs):
                        pygame.time.wait(sleep)
                        return is_diagonal, False, True
                    if self._mouse_over_button(mouse, diagonal):
                        is_diagonal = not is_diagonal

    def _draw(self, mouse, is_diagonal):
        self.window.fill((255, 255, 255))
        bottom_y = self._draw_text()
        a_star = self._draw_button(mouse, bottom_y, 0, 'A*', RED)
        bfs = self._draw_button(mouse, bottom_y, 1, 'BFS', GREEN)
        dfs = self._draw_button(mouse, bottom_y, 2, 'DFS', BLUE)
        text = 'Diagonals Are Off'
        if is_diagonal:
            text = 'Diagonals Are On'
        diagonal = self._draw_diagonal_button(mouse, bottom_y, text)
        pygame.display.update()
        return a_star, bfs, dfs, diagonal

    def _draw_text(self):
        title = self._render_text('Path Finder', 'timesnewroman', 40)
        self.window.blit(title, ((self.width - title.get_width()) // 2, 10))
        controls = pygame.image.load('path_finding_controls.jpg')
        self.window.blit(
            controls, ((self.width - controls.get_width()) // 2, 20 + title.get_height()))
        bottom_y = 20 + title.get_height() + controls.get_height()
        return bottom_y

    def _draw_button(self, mouse, bottom_y, x_multiplier, text, color):
        width = self.width // 4
        height = (self.height - bottom_y) * 2 // 3
        x = width // 4 * (x_multiplier + 1) + width * x_multiplier
        y = (bottom_y + self.height) // 2 - height // 2

        if self._mouse_over_button(mouse, (x, y, width, height)):
            color = tuple([max(0, color_val - 30) for color_val in color])

        pygame.draw.rect(self.window, color,
                         (x, y, width, height), border_radius=10)

        label = self._render_text(text, 'timenewroman', 35)
        self.window.blit(label, (x + width // 2 - label.get_width() //
                         2, y + height // 2 - label.get_height() // 2))

        return (x, y, width, height)

    def _draw_diagonal_button(self, mouse, bottom_y, text):
        y2 = (bottom_y + self.height) // 2 - (self.height - bottom_y) // 3
        width = self.width // 4
        height = (y2 - bottom_y) // 2
        x = width // 2 + width
        y = (bottom_y + y2) // 2 - height // 2

        color = (120, 120, 120)
        if self._mouse_over_button(mouse, (x, y, width, height)):
            color = tuple([max(0, color_val - 30) for color_val in color])

        pygame.draw.rect(self.window, color,
                         (x, y, width, height), border_radius=10)

        label = self._render_text(text, 'timenewroman', 25)
        self.window.blit(label, (x + width // 2 - label.get_width() //
                         2, y + height // 2 - label.get_height() // 2))

        return (x, y, width, height)

    def _render_text(self, text, font_type, size, textcolor=(255, 255, 255), outlinecolor=(0, 0, 0), outlinepx=2):
        font = pygame.font.SysFont(font_type, size)
        textsurface = font.render(text, True, textcolor).convert_alpha()
        width = textsurface.get_width() + 2 * outlinepx
        height = font.get_height()

        outline_surf = pygame.Surface(
            (width, height + 2 * outlinepx)).convert_alpha()
        outline_surf.fill((0, 0, 0, 0))

        surf = outline_surf.copy()

        outline_surf.blit(font.render(
            text, True, outlinecolor).convert_alpha(), (0, 0))

        for dx, dy in self._circlepoints(outlinepx):
            surf.blit(outline_surf, (dx + outlinepx, dy + outlinepx))

        surf.blit(textsurface, (outlinepx, outlinepx))
        return surf

    def _circlepoints(self, r):
        # creates outline of r pixels around text
        r = int(round(r))
        if r in self.circle_cache:
            return self.circle_cache[r]
        x, y, e = r, 0, 1 - r
        self.circle_cache[r] = points = []
        while x >= y:
            points.append((x, y))
            y += 1
            if e < 0:
                e += 2 * y - 1
            else:
                x -= 1
                e += 2 * (y - x) - 1
        points += [(y, x) for x, y in points if x > y]
        points += [(-x, y) for x, y in points if x]
        points += [(x, -y) for x, y in points if y]
        points.sort()
        return points

    def _mouse_over_button(self, mouse, dimensions):
        # precondtion: mouse is not None
        # expects a single param that is a tuple of 4 ints: x pos, y pos, width, and height of button
        x, y, width, height = dimensions
        return (mouse[0] >= x and mouse[0] <= x + width) and (
            mouse[1] >= y and mouse[1] <= y + height)
