import sys


def part_a(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    energized = [[False] * width for _ in range(height)]

    beams = [(0, 0, "right")]
    cycles = set()

    while beams:
        next = []

        for i, j, direction in beams:
            if 0 <= i < height and 0 <= j < width and (i, j, direction) not in cycles:
                energized[i][j] = True
                cycles.add((i, j, direction))

                match lines[i][j]:
                    case ".":
                        match direction:
                            case "right":
                                next.append((i, j + 1, "right"))
                            case "left":
                                next.append((i, j - 1, "left"))
                            case "up":
                                next.append((i - 1, j, "up"))
                            case "down":
                                next.append((i + 1, j, "down"))
                    case "|":
                        match direction:
                            case "right":
                                next.append((i - 1, j, "up"))
                                next.append((i + 1, j, "down"))
                            case "left":
                                next.append((i - 1, j, "up"))
                                next.append((i + 1, j, "down"))
                            case "up":
                                next.append((i - 1, j, "up"))
                            case "down":
                                next.append((i + 1, j, "down"))
                    case "-":
                        match direction:
                            case "right":
                                next.append((i, j + 1, "right"))
                            case "left":
                                next.append((i, j - 1, "left"))
                            case "up":
                                next.append((i, j + 1, "right"))
                                next.append((i, j - 1, "left"))
                            case "down":
                                next.append((i, j + 1, "right"))
                                next.append((i, j - 1, "left"))
                    case "\\":
                        match direction:
                            case "right":
                                next.append((i + 1, j, "down"))
                            case "left":
                                next.append((i - 1, j, "up"))
                            case "up":
                                next.append((i, j - 1, "left"))
                            case "down":
                                next.append((i, j + 1, "right"))
                    case "/":
                        match direction:
                            case "right":
                                next.append((i - 1, j, "up"))
                            case "left":
                                next.append((i + 1, j, "down"))
                            case "up":
                                next.append((i, j + 1, "right"))
                            case "down":
                                next.append((i, j - 1, "left"))

        beams = next

    result = sum([sum(x) for x in energized])
    print(result)


def part_b(lines: list[str]):
    height = len(lines)
    width = len(lines[0])
    result = 0

    start_down = [(0, j, "down") for j in range(width)]
    start_up = [(height - 1, j, "up") for j in range(width)]
    start_right = [(i, 0, "right") for i in range(height)]
    start_left = [(i, width - 1, "left") for i in range(height)]
    starting_conditions = []
    starting_conditions.extend(start_down)
    starting_conditions.extend(start_up)
    starting_conditions.extend(start_right)
    starting_conditions.extend(start_left)

    for start in starting_conditions:
        beams = [start]

        energized = [[False] * width for _ in range(height)]
        cycles = set()

        while beams:
            next = []

            for i, j, direction in beams:
                if (
                    0 <= i < height
                    and 0 <= j < width
                    and (i, j, direction) not in cycles
                ):
                    energized[i][j] = True
                    cycles.add((i, j, direction))

                    match lines[i][j]:
                        case ".":
                            match direction:
                                case "right":
                                    next.append((i, j + 1, "right"))
                                case "left":
                                    next.append((i, j - 1, "left"))
                                case "up":
                                    next.append((i - 1, j, "up"))
                                case "down":
                                    next.append((i + 1, j, "down"))
                        case "|":
                            match direction:
                                case "right":
                                    next.append((i - 1, j, "up"))
                                    next.append((i + 1, j, "down"))
                                case "left":
                                    next.append((i - 1, j, "up"))
                                    next.append((i + 1, j, "down"))
                                case "up":
                                    next.append((i - 1, j, "up"))
                                case "down":
                                    next.append((i + 1, j, "down"))
                        case "-":
                            match direction:
                                case "right":
                                    next.append((i, j + 1, "right"))
                                case "left":
                                    next.append((i, j - 1, "left"))
                                case "up":
                                    next.append((i, j + 1, "right"))
                                    next.append((i, j - 1, "left"))
                                case "down":
                                    next.append((i, j + 1, "right"))
                                    next.append((i, j - 1, "left"))
                        case "\\":
                            match direction:
                                case "right":
                                    next.append((i + 1, j, "down"))
                                case "left":
                                    next.append((i - 1, j, "up"))
                                case "up":
                                    next.append((i, j - 1, "left"))
                                case "down":
                                    next.append((i, j + 1, "right"))
                        case "/":
                            match direction:
                                case "right":
                                    next.append((i - 1, j, "up"))
                                case "left":
                                    next.append((i + 1, j, "down"))
                                case "up":
                                    next.append((i, j + 1, "right"))
                                case "down":
                                    next.append((i, j - 1, "left"))

            beams = next

        result = max(result, sum([sum(x) for x in energized]))

    print(result)
    pass


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
