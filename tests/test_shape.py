from src.shapes import ShapeS
from src.shapes.shape import Cell


def test_build_correct_size():
    s = ShapeS()
    handle = Cell(0, 0)
    cells = s.build(handle)
    assert len(cells) == 5


def test_build_correct_set():
    s = ShapeS()
    handle = Cell(2, 0)
    cells = s.build(handle)
    assert cells == set(
        (
            Cell(0, 0),
            Cell(x=-1, y=1),
            Cell(x=-1, y=0),
            Cell(x=-2, y=2),
            Cell(x=-1, y=2),
        )
    )
