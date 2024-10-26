"""Primary shape module"""

from .shape import Cell, Shape


class ShapeO(Shape):
    """Class for primary shape (1 cell)."""

    shape_id = 5
    name = "O"
    schema = "X"

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(2, 0),
        ]
        self._set_variations()
