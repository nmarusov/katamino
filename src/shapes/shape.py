"""Base shape class module."""

from collections import namedtuple

Cell = namedtuple("Cell", "x y")


class Shape:
    """Base class for shapes."""

    shape_id = 0
    name = ""
    schema = ""

    def __init__(self):
        self.schema = self.schema.strip("\n")
        self.handles = []  # manipulation points
        self.variations = set()

    def _set_variations(self):
        """Precalculates all possible orientations of this shape."""
        self.variations = list(self.orientations())

    def build(self, handle: Cell) -> set[Cell]:
        """Builds a shape from schema."""
        return set(
            Cell(x - handle.x, y - handle.y)
            for y, row in enumerate(self.schema.split("\n"))
            for x, c in enumerate(row)
            if c != " "
        )

    @staticmethod
    def rotate(cells: set[Cell], times=1):
        """Rotates the shape given number of times around (0, 0)."""
        new_cells = set()

        for cell in cells:
            x, y = cell.x, cell.y

            for _ in range(times):
                x, y = -y, x

            new_cells.add(Cell(x, y))

        return new_cells

    @staticmethod
    def flip(cells: set[Cell]):
        """Flip the shape relative to x axis."""
        new_cells = set()

        for cell in cells:
            x, y = cell.x, cell.y
            new_cells.add(Cell(-x, y))

        return new_cells

    def __str__(self):
        return self.schema

    def orientations(self):
        """Rotation & flips generator."""
        accepted = []

        # For each handle (manipulation point)
        for handle in self.handles:
            cells = self.build(handle)

            # 4 rotations, 2 flips
            for n in range(4):
                rotated = self.rotate(cells, n)
                # Test if shape lays on the right side of the handle
                # Exclude duplicated orientations
                if all(c.x >= 0 for c in rotated) and rotated not in accepted:
                    accepted.append(rotated)
                    yield rotated

                flipped = self.flip(rotated)
                # Test if shape lays on the right side of the handle
                # Exclude duplicated orientations
                if all(c.x >= 0 for c in cells) and rotated not in accepted:
                    accepted.append(flipped)
                    yield flipped
