import pygame
import random
from spot import Spot


class Grid:
    def __init__(self, cols, rows, width):
        self.cols = cols
        self.rows = rows
        self.width = width
        self.grid = []
        for col in range(self.cols):
            column = []
            for row in range(self.rows):
                column.append(Spot(col, row, self.width))
            self.grid.append(column)

    def draw(self, window):
        # draw spots
        for col in range(self.cols):
            for row in range(self.rows):
                self.grid[col][row].draw(window)
        # draw grid lines
        grey = (120, 120, 120)
        for i in range(self.cols):
            pygame.draw.line(window, grey, (i * self.width, 0),
                             (i * self.width, self.rows * self.width))
        for i in range(self.cols):
            pygame.draw.line(window, grey, (0, i * self.width),
                             (self.cols * self.width, i * self.width))
        pygame.display.update()

    # rests anything not a barrier or start or end
    def soft_reset(self):
        for col in range(self.cols):
            for row in range(self.rows):
                spot = self.grid[col][row]
                if not spot.is_barrier() and not spot.is_start() and not spot.is_end():
                    spot.reset()

    def non_barrier_reset(self):
        for col in range(self.cols):
            for row in range(self.rows):
                spot = self.grid[col][row]
                if not spot.is_barrier():
                    spot.reset()

    def reset(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.grid[col][row].reset()

    def randomize_barriers(self, start, end):
        if start is None:
            while True:
                rand_col = random.randrange(self.cols)
                rand_row = random.randrange(self.rows)
                if self.grid[rand_col][rand_row] is not end:
                    start = self.grid[rand_col][rand_row]
                    start.make_start()
                    break
        if end is None:
            while True:
                rand_col = random.randrange(self.cols)
                rand_row = random.randrange(self.rows)
                if self.grid[rand_col][rand_row] is not start:
                    end = self.grid[rand_col][rand_row]
                    end.make_end()
                    break

        for col in range(self.cols):
            for row in range(self.rows):
                if random.random() < 0.2 and not self.grid[col][row].is_start() and not self.grid[col][row].is_end():
                    self.grid[col][row].make_barrier()
        return start, end
