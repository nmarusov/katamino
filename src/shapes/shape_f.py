"""F-shape module"""

from .shape import Cell, Shape


class ShapeF(Shape):
    """Class for F-shape."""

    shape_id = 2
    name = "F"
    schema = """
XX
XX
X
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(0, 0),
            Cell(1, 0),
            Cell(0, 2),
        ]
        self._set_variations()
