import random
import re
from levelz.coord import Coordinate2D, Coordinate3D
from levelz.block import Block, LevelObject
from levelz.level import Level2D, Level3D

# Export

HEADER_END = "---"
"""The end of the Header section."""

END = "end"
"""The end of a Level."""

def parse_level(level: str):
    """Parses a Level from a string. Uses '\\n' as the line separator."""

    lines = level.split("\n")
    return parse_lines(lines)
    
def parse_file(file: str):
    """Parses a Level from a file."""

    f=open(file, "r")
    lines0 = f.readlines()
    f.close()

    lines = []
    for line in lines0:
        lines.append(line.strip().replace("\n", "").replace("\r", ""))

    return parse_lines(lines)

def parse_lines(level: list[str]):
    """Parses a Level from a list of strings."""

    headers0, blocks0 = __split(level)

    headers = __readHeaders(headers0)
    is2D = headers['type'] == 2

    spawn = headers['spawn']
    if (spawn == None or spawn == "default"):
        headers['spawn'] = "[0, 0]" if is2D else "[0, 0, 0]"
    
    if (is2D and 'scroll' not in headers.keys()):
        headers['scroll'] = "none"
    
    blocks = []
    for line in blocks0:
        if (line == END): break
        
        block, points = __readLine(line, not is2D)
        if (block == None or points == None): continue
        if (not isinstance(block, Block)): continue

        for point in points:
            blocks.append(LevelObject(block, point))
    
    return Level2D(headers, blocks) if is2D else Level3D(headers, blocks)
    

# Internal
    
def __split(level: list[str]):
    l = level.index("---")
    return [level[:l], level[l+1:]]

def __objectify(input: str):
    if (input.lower() == "true" or input.lower() == "false"):
        return input.lower() in ["true"]

    try:
        return int(input)
    except ValueError:
        try:
            return float(input)
        except ValueError:
            return input

def __roll(blocks: list[Block], chances: list[float]):
    sum = 0

    for value in chances:
        sum += value

    if (sum != 1):
        raise ValueError(f"Invalid Probabilities: {map}")
    
    t = None
    cumulative = 0
    r = random.random()

    for key, value in zip(blocks, chances):
        cumulative += value

        if (r < cumulative / sum):
            t = key
            break
    
    return t

def __readHeaders(headers: list[str]):
    map: dict[str, object] = {}

    for header in headers:
        if (len(header)) == 0: continue
        if (header[0] != '@'):
            raise ValueError(f"Invalid header; does not stard with @: {header}")
        
        split = re.split(r"\s(.*)", header)
        key = split[0]; value = split[1]

        map[key[1:]] = __objectify(value)
    
    if (map['type'] == None): raise ValueError("Missing @type header")
    if (map['type'] != 2 and map['type'] != 3): raise ValueError(f"Invalid @type header")
    if (map['spawn'] == None): raise ValueError("Missing @spawn header")

    return map

def __read2DPoints(input: str):
    points: list[Coordinate2D] = []

    inputs = re.split(r"\*", input)

    for s0 in inputs:
        s = s0.strip()
        if (len(s) == 0): continue

        if (s[0] == '(' and s[-1] == ']'):
            split = re.split(r"\^", s)

            coords = re.sub(r"[\[\]\s]", "", split[1]).split(",")
            matrix = re.sub(r"[()\s]", "", split[0]).split(",")

            if (len(coords) != 2): raise ValueError(f"Invalid 2D Coordinate: {s}")
            if (len(matrix) != 4): raise ValueError(f"Invalid 2D Matrix: {s}")

            cx = float(coords[0]); cy = float(coords[1])
            x1 = int(matrix[0]); x2 = int(matrix[1])
            y1 = int(matrix[2]); y2 = int(matrix[3])

            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    points.append(Coordinate2D(cx + x, cy + y))
        else:
            points.append(Coordinate2D.from_string(s))
    
    return points

def __read3DPoints(input: str):
    points: list[Coordinate3D] = []

    inputs = re.split(r"\*", input)

    for s0 in inputs:
        s = s0.strip()
        if (len(s) == 0): continue

        if (s[0] == '(' and s[-1] == ']'):
            split = re.split(r"\^", s)

            coords = re.sub(r"[\[\]\s]", "", split[1]).split(",")
            matrix = re.sub(r"[()\s]", "", split[0]).split(",")

            if (len(coords) != 3): raise ValueError(f"Invalid 3D Coordinate: {s}")
            if (len(matrix) != 6): raise ValueError(f"Invalid 3D Matrix: {s}")

            cx = float(coords[0]); cy = float(coords[1]); cz = float(coords[2])
            x1 = int(matrix[0]); x2 = int(matrix[1])
            y1 = int(matrix[2]); y2 = int(matrix[3])
            z1 = int(matrix[4]); z2 = int(matrix[5])

            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    for z in range(min(z1, z2), max(z1, z2) + 1):
                        points.append(Coordinate3D(cx + x, cy + y, cz + z))
        else:
            points.append(Coordinate3D.from_string(s))
    
    return points

def __readLine(input: str, threeD: bool = False):
    if (len(input) == 0): return (None, None)

    split = re.sub(r"\s", "", input).split(":")
    block = __readBlock(split[0])
    if (block == None): return (None, None)

    points = __read3DPoints(split[1]) if threeD else __read2DPoints(split[1])

    return (block, points)

def __readBlock(line: str):
    if (len(line) == 0): return None

    if (line[0] == '{' and line[-1] == '}'):
        block0 = re.sub(r"[{}]", "", line)

        blocks = {}
        if ">," in line:
            blocks = re.split(r">,", block0)
            for i in range(len(blocks) - 1):
                if "<" in blocks[i]:
                    blocks[i] = f"{blocks[i]}>"
        else:
            blocks = block0.split(',')
        
        l = len(blocks)
        bls: list[Block] = []
        chances: list[float] = []

        for s in blocks:
            bl0 = s.split("=", 2)

            try:
                v = float(bl0[0])
                bl = __readRawBlock(bl0[1])
                if (bl == None): continue

                bls.append(bl)
                chances.append(v)
            except ValueError:
                bl = __readRawBlock(s)
                if (bl == None): continue

                bls.append(bl)
                chances.append(1 / l)
        
        return __roll(bls, chances)
    else:
        return __readRawBlock(line)

def __readRawBlock(input: str):
    if (len(input) == 0): return None

    split = re.sub(r"[\s>]", "", input).split("<")
    name = split[0].strip()

    if (len(split) == 1): return Block(name)

    properties = {}
    rawProperties = split[1].split(",")

    for s in rawProperties:
        key, value = s.split("=")
        properties[key] = __objectify(value)
    
    return Block(name, properties)