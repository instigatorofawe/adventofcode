import sys


def get_position(lines: list[str]) -> tuple[int, int]:
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                return i, j


def detect_cycle(lines: list[str]) -> bool:
    height = len(lines)
    width = len(lines[0])

    i, j = get_position(lines)
    direction = "up"

    cycle_detection = set()

    while 0 <= i < height and 0 <= j < width:
        if (i, j, direction) in cycle_detection:
            return True
        cycle_detection.add((i, j, direction))
        match direction:
            case "up":
                x, y = i - 1, j
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "right"
            case "right":
                x, y = i, j + 1
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "down"
            case "down":
                x, y = i + 1, j
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "left"
            case "left":
                x, y = i, j - 1
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "up"
        i, j = x, y
    return False


def part_a(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    occupied = [[False for _ in range(width)] for _ in range(height)]

    i, j = get_position(lines)
    direction = "up"

    while 0 <= i < height and 0 <= j < width:
        occupied[i][j] = True
        match direction:
            case "up":
                x, y = i - 1, j
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "right"
            case "right":
                x, y = i, j + 1
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "down"
            case "down":
                x, y = i + 1, j
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "left"
            case "left":
                x, y = i, j - 1
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "up"
        i, j = x, y

    result = 0
    for line in occupied:
        result += sum(line)

    print(result)


def part_b(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    occupied = [[False for _ in range(width)] for _ in range(height)]

    i, j = get_position(lines)
    direction = "up"

    while 0 <= i < height and 0 <= j < width:
        occupied[i][j] = True
        match direction:
            case "up":
                x, y = i - 1, j
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "right"
            case "right":
                x, y = i, j + 1
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "down"
            case "down":
                x, y = i + 1, j
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "left"
            case "left":
                x, y = i, j - 1
                if 0 <= x < height and 0 <= y < width and lines[x][y] == "#":
                    x, y = i, j
                    direction = "up"
        i, j = x, y

    candidates = [
        (i, j)
        for i in range(height)
        for j in range(width)
        if occupied[i][j] and lines[i][j] == "."
    ]

    result = 0
    for i, j in candidates:
        lines[i][j] = "#"
        result += detect_cycle(lines)
        lines[i][j] = "."

    print(result)


def run():
    lines = [[x for x in line.strip()] for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
