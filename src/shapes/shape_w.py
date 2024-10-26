"""W-shape module"""

from .shape import Cell, Shape


class ShapeW(Shape):
    """Class for W-shape."""

    shape_id = 10
    name = "W"
    schema = """
X
XX
 XX
    """

    def __init__(self):
        super().__init__()
        self.handles = [Cell(0, 0)]
        self._set_variations()
