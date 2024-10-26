"""Q-shape module"""

from .shape import Cell, Shape


class ShapeQ(Shape):
    """Class for Q-shape."""

    shape_id = 6
    name = "Q"
    schema = """
 XX
XX
 X
    """

    def __init__(self):
        super().__init__()
        self.handles = [
            Cell(2, 0),
            Cell(0, 1),
            Cell(1, 2),
        ]
        self._set_variations()
