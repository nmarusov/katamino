"""Y-shape module"""

from .shape import Cell, Shape


class ShapeY(Shape):
    """Class for Y-shape."""

    shape_id = 11
    name = "Y"
    schema = """
X
XX
X
X
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(0, 0),
            Cell(1, 1),
            Cell(0, 3),
        ]
        self._set_variations()
