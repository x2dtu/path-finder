import pygame
import sys

from grid import Grid
from a_star import A_star
from bfs import Bfs
from dfs import Dfs
from menu import Menu

pygame.init()

ROWS, COLS = 50, 50
SPOT_WIDTH = 15

WIDTH, HEIGHT = COLS * SPOT_WIDTH, ROWS * SPOT_WIDTH

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Path Finder')

FPS = 100


def get_pos_mouse(pos):
    return pos[0] // SPOT_WIDTH, pos[1] // SPOT_WIDTH


def make_path(start, end):
    curr = end
    while curr.parent:
        curr.parent.make_path()
        curr = curr.parent
    start.make_start()
    end.make_end()


def main():
    clock = pygame.time.Clock()
    menu = Menu(WINDOW, lambda: clock.tick(FPS))
    grid = Grid(COLS, ROWS, SPOT_WIDTH)
    start, end = None, None
    # start with True arg for Diagonals Are On
    is_diagonal, bfs, dfs = menu.run(True)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and start and end:
                    grid.soft_reset()
                    algorithm = None
                    if bfs:
                        algorithm = Bfs(start, end, grid, WINDOW,
                                        lambda: clock.tick(FPS), is_diagonal)
                    elif dfs:
                        algorithm = Dfs(start, end, grid, WINDOW,
                                        lambda: clock.tick(FPS), is_diagonal)
                    else:
                        algorithm = A_star(
                            start, end, grid, WINDOW, lambda: clock.tick(FPS), is_diagonal)
                    if algorithm.solve():
                        make_path(start, end)
                    else:
                        start.reset()
                        end.reset()
                        start, end = None, None
                elif event.key == pygame.K_c:
                    grid.reset()
                    start, end = None, None
                elif event.key == pygame.K_x:
                    grid.non_barrier_reset()
                    start, end = None, None
                elif event.key == pygame.K_r:
                    start, end = grid.randomize_barriers(start, end)
                elif event.key == pygame.K_a:
                    bfs, dfs = False, False  # use A*
                elif event.key == pygame.K_b:
                    bfs, dfs = True, False  # use BFS
                elif event.key == pygame.K_d:
                    bfs, dfs = False, True  # use DFS
                elif event.key == pygame.K_ESCAPE:
                    is_diagonal, bfs, dfs = menu.run(is_diagonal)

        if pygame.mouse.get_pressed()[0]:  # left mouse button
            col, row = get_pos_mouse(pygame.mouse.get_pos())
            spot = grid.grid[col][row]
            if not start and spot != end:
                start = spot
                start.make_start()
            elif not end and spot != start:
                end = spot
                end.make_end()
            elif spot != start and spot != end:
                spot.make_barrier()
        elif pygame.mouse.get_pressed()[2]:  # right mouse button
            col, row = get_pos_mouse(pygame.mouse.get_pos())
            spot = grid.grid[col][row]
            spot.reset()
            if spot == start:
                start = None
            elif spot == end:
                end = None

        grid.draw(WINDOW)


if __name__ == "__main__":
    main()
