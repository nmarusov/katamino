"""C-shape module"""

from .shape import Cell, Shape


class ShapeC(Shape):
    """Class for C-shape."""

    shape_id = 1
    name = "C"
    schema = """
XX
X
XX
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(1, 0),
        ]
        self._set_variations()
