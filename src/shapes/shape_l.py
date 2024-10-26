"""L-shape module"""

from .shape import Cell, Shape


class ShapeL(Shape):
    """Class for L-shape."""

    shape_id = 4
    name = "L"
    schema = """
X
X
X
XX
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(0, 0),
            Cell(0, 3),
            Cell(1, 3),
        ]
        self._set_variations()
