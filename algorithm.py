import pygame
import sys


class Algorithm:
    def __init__(self, start, end, grid, window, clock, is_diagonal):
        self.start = start
        self.end = end
        self.grid = grid
        self.window = window
        self.clock = clock
        self.is_diagonal = is_diagonal

    def check_stop_events_and_tick(self):
        self.clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.grid.reset()
                    self.start, self.end = None, None
                    return False
                if event.key == pygame.K_x:
                    self.grid.non_barrier_reset()
                    self.start, self.end = None, None
                    return False
        return True
