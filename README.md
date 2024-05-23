# levelz-py

> Python bindings & API for the LevelZ File Format

![GitHub Release](https://img.shields.io/github/v/release/LevelZ-File/py-bindings)

## Overview

Provides Python Parsing/Support for the LevelZ File Format. 

## Download

```bash
pip install levelz-py
```

## Usage

```py
from levelz import Coordiante2D

coord = Coordiante2D(1, 2)
print(coord)
```

```py
from levelz import parse_lines, Level2D

lines = [
    "@type 2",
    "@spawn default",
    "---",
    "grass: [0, 0]*[0, 1]"
]

level: Level2D = parse_lines(lines)
```

```py
from levelz import parse_file

level = parse_file("level.lvlz")
print(level)
```