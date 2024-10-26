"""S-shape module"""

from .shape import Cell, Shape


class ShapeS(Shape):
    """Class for S-shape."""

    shape_id = 7
    name = "S"
    schema = """
 XX
 X
XX
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(2, 0),
            Cell(0, 2),
        ]
        self._set_variations()
