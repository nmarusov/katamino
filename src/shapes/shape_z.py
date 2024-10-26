"""Z-shape module"""

from .shape import Cell, Shape


class ShapeZ(Shape):
    """Class for Z-shape."""

    shape_id = 12
    name = "Z"
    schema = """
XX
 XXX
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(0, 0),
            Cell(3, 1),
        ]
        self._set_variations()
