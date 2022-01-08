from algorithm import Algorithm
import itertools


class Dfs(Algorithm):
    def __init__(self, start, end, grid, window, clock, is_diagonal):
        super().__init__(start, end, grid, window, clock, is_diagonal)

    def solve(self):
        stack = [self.start]
        visited_set = {self.start}  # set originally containing the start spot

        self.populate_neighbors()
        return self.solve_loop(stack, visited_set)

    def solve_loop(self, stack, visited_set):
        while stack:
            if not self.check_stop_events_and_tick():
                return False
            current = stack.pop()
            if current is self.end:
                print("Finished")
                return True  # we found it

            for neighbor in current.neighbors:
                if neighbor not in visited_set:
                    neighbor.parent = current
                    if neighbor is self.end:
                        return True
                    stack.append(neighbor)
                    visited_set.add(neighbor)
                    neighbor.make_open()

            # now that we are done analyzing neighbors of current, make it closed
            if current is not self.start:
                current.make_closed()

            self.grid.draw(self.window)

        return False  # we couldn't find a path

    def populate_neighbors(self):
        for col in range(self.grid.cols):
            for row in range(self.grid.rows):
                spot = self.grid.grid[col][row]
                if not spot.is_barrier():
                    spot.add_neighbors(self.grid.grid)
                    if self.is_diagonal:
                        total_neighbors = itertools.zip_longest(
                            spot.diagonal_neighbors, spot.neighbors)
                        total_neighbors = list(
                            itertools.chain(*total_neighbors))
                        spot.neighbors = [
                            neighbor for neighbor in total_neighbors if neighbor is not None]
