# Katamino solver
## Usage

```
Usage: main.py [OPTIONS] FILENAME

Options:
  -l, --level INTEGER  Level (field width).
  -g, --greedy         Save all solutions for each shape set(rotated, flipped,
                       alternative).
  --help               Show this message and exit.
```

## Shapes

### C
```
XX
X
XX
```

### F
```
XX
XX
X
```

### L
```
X
X
X
XX
```

### Q
```
 XX
XX
 X
```

### S
```
 XX
 X
XX
```

### T
```
XXX
 X
 X
```

### V
```
X
X
XXX
```

### W
```
X
XX
 XX
```

### Y
```
X
XX
X
X
```

### Z
```
XX
 XXX
```

### Other: I and O
```
X
X
```
```
X
```

You can add custom shapes to /shapes folder and add it common shape set in solver.py:
```python
SHAPES = {
    shapes.ShapeC(),
    shapes.ShapeF(),
    # shapes.ShapeI(),
    shapes.ShapeL(),
    # shapes.ShapeO(),
    shapes.ShapeQ(),
    shapes.ShapeS(),
    shapes.ShapeT(),
    shapes.ShapeV(),
    shapes.ShapeW(),
    shapes.ShapeY(),
    shapes.ShapeZ(),
}
```