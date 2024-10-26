"""Katamino field model module."""

from shapes.shape import Cell


def call_counter(func):
    """Counts the number of calls to the function."""
    counter = 0

    def inner(*args, **kwargs):
        nonlocal counter
        result = func(*args, **kwargs)
        counter += 1
        if counter % 10000 == 0:
            print(counter)
        return result

    return inner


class Field:
    """Katamino field model."""

    def __init__(self, level=3):
        assert 3 <= level <= 12, "Level must be in 3...12"
        self.height = 5
        self.width = level
        # Fill the field with empty cells
        # Cell will be filled with shape IDs
        self.cells = [
            [0 for x in range(self.width)] for y in range(self.height)
        ]
        self.history = []

    # @call_counter
    def fit(self, cell: Cell, shape: set[Cell]):
        """Tests whether the shape fits the empty cells."""
        # Check if the shape fits in the field
        left = min(c.x for c in shape)
        right = max(c.x for c in shape)
        bottom = min(c.y for c in shape)
        top = max(c.y for c in shape)

        if (
            left + cell.x < 0
            or right + cell.x >= self.width
            or top + cell.y >= self.height
            or bottom + cell.y < 0
        ):
            return False

        # Check if the shape fits in the vacant cells
        for x, y in shape:
            if self.cells[y + cell.y][x + cell.x] != 0:
                return False

        return True

    def place_shape(self, cell: Cell, shape: set[Cell], shape_id):
        """Places the shape to the field."""
        record = {
            "shape": shape,
            "cell": cell,
        }

        for x, y in shape:
            x_ = x + cell.x
            y_ = y + cell.y
            self.cells[y_][x_] = shape_id

        self.history.append(record)

    def remove_last_shape(self):
        """Removes last shape from the field."""
        record = self.history.pop()
        shape = record["shape"]
        cell = record["cell"]

        for x, y in shape:
            self.cells[y + cell.y][x + cell.x] = 0

    def is_column_filled(self, x: int) -> bool:
        """Checks if the column x is filled."""
        return all(row[x] != 0 for row in self.cells)

    def format(self, markers):
        """Prepares the field for printing."""
        image = []

        for row in self.cells:
            line = "".join(
                markers[shape_id] if shape_id != 0 else " " for shape_id in row
            )
            image.append(line)

        return "\n".join(image)

    def vacant_cells(self, x: int):
        """Generator of vacant cells in column x."""
        for y in range(self.height):
            if self.cells[y][x] == 0:
                yield Cell(x, y)

    @property
    def first_vacant_column(self):
        """Returns the first vacant column."""
        for x in range(self.width):
            if not self.is_column_filled(x):
                return x
        return 0
