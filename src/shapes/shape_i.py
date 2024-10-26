"""I-shape module"""

from .shape import Cell, Shape


class ShapeI(Shape):
    """Class for I-shape (2 cells)."""

    shape_id = 3
    name = "I"
    schema = """
X
X
    """

    def __init__(self):
        super().__init__()
        self.handles = [Cell(0, 0)]
        self._set_variations()
