"""V-shape module"""

from .shape import Cell, Shape


class ShapeV(Shape):
    """Class for V-shape."""

    shape_id = 9
    name = "V"
    schema = """
X
X
XXX
    """

    def __init__(self):
        super().__init__()
        self.handles = [Cell(0, 0), Cell(0, 2), Cell(2, 2)]
        self._set_variations()
