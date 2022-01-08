import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 130, 255)
ORANGE = (255, 116, 0)
RED = (255, 30, 30)
GREEN = (40, 210, 40)
PURPLE = (204, 0, 204)


class Spot:
    def __init__(self, col, row, width):
        self.x = col * width
        self.y = row * width
        self.width = width
        self.col, self.row = col, row
        self.neighbors = []
        self.diagonal_neighbors = []
        self.color = WHITE
        self.parent = None

    def make_barrier(self):
        self.color = BLACK

    def is_barrier(self):
        return self.color == BLACK

    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_path(self):
        self.color = PURPLE

    def make_start(self):
        self.color = BLUE

    def is_start(self):
        return self.color == BLUE

    def make_end(self):
        self.color = ORANGE

    def is_end(self):
        return self.color == ORANGE

    def reset(self):
        self.color = WHITE
        self.parent = None

    def get_pos(self):
        return self.col, self.row

    def draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.width))

    def add_neighbors(self, grid):
        self.neighbors, self.diagonal_neighbors = [], []
        total_cols, total_rows = len(grid), len(grid[0])
        # left
        if self.col - 1 >= 0 and not grid[self.col - 1][self.row].is_barrier():
            self.neighbors.append(grid[self.col - 1][self.row])
        # down
        if self.row + 1 < total_rows and not grid[self.col][self.row + 1].is_barrier():
            self.neighbors.append(grid[self.col][self.row + 1])
        # right
        if self.col + 1 < total_cols and not grid[self.col + 1][self.row].is_barrier():
            self.neighbors.append(grid[self.col + 1][self.row])
        # up
        if self.row - 1 >= 0 and not grid[self.col][self.row - 1].is_barrier():
            self.neighbors.append(grid[self.col][self.row - 1])

        # diagonals

        # top left
        if self.col - 1 >= 0 and self.row - 1 >= 0 and not grid[self.col - 1][self.row - 1].is_barrier():
            self.diagonal_neighbors.append(grid[self.col - 1][self.row - 1])
        # bottom left
        if self.col - 1 >= 0 and self.row + 1 < total_rows and not grid[self.col - 1][self.row + 1].is_barrier():
            self.diagonal_neighbors.append(grid[self.col - 1][self.row + 1])
        # bottom right
        if self.col + 1 < total_cols and self.row + 1 < total_rows and not grid[self.col + 1][self.row + 1].is_barrier():
            self.diagonal_neighbors.append(grid[self.col + 1][self.row + 1])
        # top right
        if self.col + 1 < total_cols and self.row - 1 >= 0 and not grid[self.col + 1][self.row - 1].is_barrier():
            self.diagonal_neighbors.append(grid[self.col + 1][self.row - 1])

    def __lt__(self, other):
        return self.col < other.col and self.row < other.row

    def __repr__(self):
        return f"col: {self.col}, row: {self.row}, {self.color}"
