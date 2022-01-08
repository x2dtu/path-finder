from algorithm import Algorithm
from queue import PriorityQueue


class A_star(Algorithm):
    def __init__(self, start, end, grid, window, clock, is_diagonal):
        super().__init__(start, end, grid, window, clock, is_diagonal)

    def h(self, current):
        # manhattan distance between current spot and end spot
        curr_col, curr_row = current.get_pos()
        end_col, end_row = self.end.get_pos()
        return abs(end_col - curr_col) + abs(end_row - curr_row)

    def solve(self):
        # set g and f scores for each spot to infinity
        g_score = {spot: float("inf")
                   for col in self.grid.grid for spot in col}
        f_score = {spot: float("inf")
                   for col in self.grid.grid for spot in col}

        g_score[self.start] = 0  # start is 0 away from start
        f_score[self.start] = self.h(self.start)  # g_score (0) + h_score

        open_priority_queue = PriorityQueue()
        # we will put tuples containing f score, count, and the Spot into priority queue
        # start off with 0 f score, 0 count, and starting Spot
        open_priority_queue.put((0, 0, self.start))

        open_set = {self.start}  # set originally containing the start spot

        return self.solve_loop(open_priority_queue, open_set, g_score, f_score)

    def solve_loop(self, open_priority_queue, open_set, g_score, f_score):
        count = 0

        while not open_priority_queue.empty():
            if not self.check_stop_events_and_tick():
                return False

            # gets the highest priority tuple, and the second index of that tuple which will be the Spot
            current = open_priority_queue.get()[2]
            # we are looking at current, so remove it from open set
            open_set.remove(current)

            if current is self.end:
                return True  # we found it

            current.add_neighbors(self.grid.grid)
            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1
                # unless g_score[neighbor] has already been calculated, it will be inf
                self.update_scores(temp_g_score, current, neighbor,
                                   g_score, f_score, count, open_priority_queue, open_set)

            if self.is_diagonal:
                for neighbor in current.diagonal_neighbors:
                    temp_g_score = g_score[current] + 1.4
                    self.update_scores(temp_g_score, current, neighbor,
                                       g_score, f_score, count, open_priority_queue, open_set)

            # now that we are done analyzing neighbors of current, make it closed
            if current is not self.start:
                current.make_closed()

            self.grid.draw(self.window)

        return False  # we couldn't find a path

    def update_scores(self, temp_g_score, current, neighbor, g_score, f_score, count, open_priority_queue, open_set):
        if temp_g_score < g_score[neighbor]:
            # reassign parent of neighbor to current since current is closest to it
            neighbor.parent = current
            g_score[neighbor] = temp_g_score
            f_score[neighbor] = temp_g_score + self.h(neighbor)
            if neighbor not in open_set:
                open_set.add(neighbor)
                count += 1
                open_priority_queue.put(
                    (f_score[neighbor], count, neighbor))
                neighbor.make_open()
