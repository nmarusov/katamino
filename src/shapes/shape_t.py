"""T-shape module"""

from .shape import Cell, Shape


class ShapeT(Shape):
    """Class for T-shape."""

    shape_id = 8
    name = "T"
    schema = """
XXX
 X
 X
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(0, 0),
            Cell(1, 2),
        ]
        self._set_variations()
