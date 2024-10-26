"""Solutions visualization."""

import os
import re

from PIL import Image, ImageDraw

SOL = re.compile(
    r"(?P<header>Level: \d+, solution: \d+, tag: [CFLQSTVWYZIO]+)\n(?P<solution>[CFLQSTVWYZIO\n]+)(?:-+)"
)
HEADER = re.compile(
    r"Level: (?P<level>\d+), solution: (?P<solution>\d+), tag: (?P<tag>[CFLQSTVWYZIO]+)"
)

SCALE = 0.25
ORIGIN = (104, 104)
SIZE = 109.7
COLORS = {
    "C": "#01BAFE",
    "F": "#0085FE",
    "I": "#FB5A21",
    "L": "#FF1D22",
    "O": "#FB5A21",
    "Q": "#FE6ABE",
    "S": "#33D203",
    "T": "#FBF501",
    "V": "#9B5E5D",
    "W": "#00A566",
    "Y": "#B25FE2",
    "Z": "#FF7305",
}
GAP = 1
IN_DIR = "output"
OUT_DIR = "solutions"

for filename in os.listdir(IN_DIR):
    with open(os.path.join(IN_DIR, filename), "r", encoding="utf-8") as f:
        s = f.read()

    with Image.open("assets/board.png") as board:
        for m in SOL.finditer(s):
            solution = m.group("solution").strip()
            header = m.group("header").strip()
            print(header)
            h = HEADER.match(header)
            level = h.group("level")
            sol = h.group("solution")
            tag = h.group("tag")

            draw = ImageDraw.Draw(board)

            for y, row in enumerate(solution.split("\n")):
                for x, shape in enumerate(row):
                    xy = (
                        (
                            ORIGIN[0] + SIZE * x + GAP,
                            ORIGIN[1] + SIZE * y + GAP,
                        ),
                        (
                            ORIGIN[0] + SIZE * (x + 1) - GAP,
                            ORIGIN[1] + SIZE * (y + 1) - GAP,
                        ),
                    )
                    draw.rectangle(xy, fill=COLORS[shape])
            output = board.resize([int(s * SCALE) for s in board.size])
            output.save(
                os.path.join(OUT_DIR, f"{level}_{sol}_{tag}.png"), "PNG"
            )
