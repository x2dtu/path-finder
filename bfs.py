from algorithm import Algorithm
from queue import Queue


class Bfs(Algorithm):
    def __init__(self, start, end, grid, window, clock, is_diagonal):
        super().__init__(start, end, grid, window, clock, is_diagonal)

    def solve(self):
        queue = Queue()
        queue.put(self.start)
        visited_set = {self.start}  # set originally containing the start spot

        return self.solve_loop(queue, visited_set)

    def solve_loop(self, queue, visited_set):
        while not queue.empty():
            if not self.check_stop_events_and_tick():
                return False

            current = queue.get()  # pops and retrieves first-in spot
            if current is self.end:
                return True  # we found it

            current.add_neighbors(self.grid.grid)
            if self.is_diagonal:
                current.neighbors.extend(current.diagonal_neighbors)

            for neighbor in current.neighbors:
                if neighbor not in visited_set:
                    queue.put(neighbor)
                    visited_set.add(neighbor)
                    neighbor.parent = current
                    neighbor.make_open()

            # now that we are done analyzing neighbors of current, make it closed
            if current is not self.start:
                current.make_closed()

            self.grid.draw(self.window)

        return False  # we couldn't find a path
