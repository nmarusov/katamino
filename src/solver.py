"""Core module"""

import copy
from collections import deque
from itertools import combinations
from multiprocessing import Process, Queue, cpu_count

import shapes
from field import Field

NUM_O = 6
NUM_I = 2

SHAPES = {
    shapes.ShapeC(),
    shapes.ShapeF(),
    # shapes.ShapeI(),
    shapes.ShapeL(),
    # shapes.ShapeO(),
    shapes.ShapeQ(),
    shapes.ShapeS(),
    shapes.ShapeT(),
    shapes.ShapeV(),
    shapes.ShapeW(),
    shapes.ShapeY(),
    shapes.ShapeZ(),
}


class Solver:
    """Core buisines-logic class."""

    def __init__(self, level=3):
        self.level = level
        self.field = Field(level=self.level)

    def solutions(self, shapeset):
        """Solution generator."""

        def layouts(shapeset: deque[shapes.Shape]):
            if not shapeset:
                # Return copy of the field
                yield copy.deepcopy(self.field)

            # Iterate over all rest shapes
            for _ in range(len(shapeset)):
                # Take next shape
                shape = shapeset.pop()

                # Try to fill column by column
                for x in range(self.field.first_vacant_column, self.field.width):
                    # Iterate over all vacant cells in current column
                    for cell in self.field.vacant_cells(x):
                        # Iterate over all possible orientations of the shape
                        # around the current cell
                        for orient in shape.variations:
                            if self.field.fit(cell, orient):
                                # If fit, place the shape and try
                                # to fill the rest of the field
                                self.field.place_shape(cell, orient, shape.shape_id)
                                yield from layouts(shapeset)
                                self.field.remove_last_shape()

                    # Cannot place current shape in current column
                    if not self.field.is_column_filled(x):
                        # Try next shape
                        break

                # Return the shape to the queue
                shapeset.appendleft(shape)

        yield from layouts(deque(shapeset))

    def format(self, solution: Field):
        """Formats solution for output."""
        return solution.format({s.shape_id: s.name for s in SHAPES})


def worker(input_q, output_q):
    """Solution worker."""
    while True:
        # Receive next shapeset
        shapeset = input_q.get()

        # No more sets to process
        if shapeset is None:
            output_q.put(None)
            break

        # New solver for each shapeset
        solver = Solver(level=len(shapeset))

        for s in solver.solutions(shapeset):
            # Discard empty solutions
            if s:
                # Return solution in string format
                output_q.put(solver.format(s))


def generate_shapesets(queue, level, n_workers):
    """Each task corresponds to the specific combination
    of shapes in the amount of $level pieces."""
    for shapeset in combinations(SHAPES, level):
        queue.put(shapeset)

    # Add sentinels to the queue
    for _ in range(n_workers):
        queue.put(None)


def solve(level=3):
    """Starts the solver."""
    n_workers = cpu_count()
    input_q = Queue()
    output_q = Queue()

    generate_shapesets(input_q, level, n_workers)

    # Create and start solution workers
    workers = [
        Process(target=worker, args=(input_q, output_q)) for _ in range(n_workers)
    ]
    for w in workers:
        w.start()

    # Receive results from the queue
    finished = 0
    while True:
        s = output_q.get()

        if s is not None:
            # Here is the next solution
            yield s
        else:
            # Ensure all workers are done with their work
            finished += 1
            if finished == n_workers:
                break

    # Finish all workers
    for w in workers:
        w.join()
