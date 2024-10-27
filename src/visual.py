"""Solutions visualization."""

import os
import re

from PIL import Image, ImageDraw

SOLUTION_RE = re.compile(
    r"Level: (?P<level>\d+), solution: (?P<index>\d+),"
    " tag: (?P<tag>[CFLQSTVWYZIO]+)\n"
    "(?P<solution>(?:[CFLQSTVWYZIO]+\n)+)"
)

IN_DIR = "output"
OUT_DIR = "solutions"

SCALE = 0.25
ORIGIN = (104, 104)
SIZE = 109.7
GAP = 1

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

print("Generating images...")

for filename in os.listdir(IN_DIR):
    with open(os.path.join(IN_DIR, filename), "r", encoding="utf-8") as f:
        s = f.read()

    with Image.open("assets/board.png") as board:
        for m in SOLUTION_RE.finditer(s):
            level = int(m.group("level"))
            index = int(m.group("index"))
            tag = m.group("tag")
            solution = m.group("solution").strip()

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
            output_filename = f"{level:02}_{index:02}_{tag}.png"
            output.save(
                os.path.join(OUT_DIR, output_filename),
                "PNG",
            )
            print(output_filename)
