import sys


def get_start(map: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(map):
        for j, c in enumerate(row):
            if c == "S":
                return (i, j)
    return (-1, -1)


def get_candidates(map: list[list[str]], i: int, j: int):
    height = len(map)
    width = len(map[0])

    north: bool = False
    east: bool = False
    south: bool = False
    west: bool = False

    # Viable directions
    if 0 <= i - 1 and map[i - 1][j] in ["|", "7", "F"]:
        north = True
    if i + 1 < height and map[i + 1][j] in ["|", "L", "J"]:
        south = True
    if 0 <= j - 1 and map[i][j - 1] in ["-", "L", "F"]:
        west = True
    if j + 1 < width and map[i][j + 1] in ["-", "7", "J"]:
        east = True

    candidates: list[str] = []

    if north and south:
        candidates.append("|")
    if east and west:
        candidates.append("-")
    if north and east:
        candidates.append("L")
    if north and west:
        candidates.append("J")
    if south and west:
        candidates.append("7")
    if south and east:
        candidates.append("F")

    return candidates


def get_next(
    map: list[list[str]], previous: tuple[int, int], current: tuple[int, int]
) -> None | tuple[int, int]:
    height = len(map)
    width = len(map[0])

    directions: list[str] = []
    y, x = current

    match map[y][x]:
        case "|":
            directions = ["south", "north"]
        case "-":
            directions = ["east", "west"]
        case "L":
            directions = ["north", "east"]
        case "J":
            directions = ["north", "west"]
        case "7":
            directions = ["south", "west"]
        case "F":
            directions = ["south", "east"]
        case _:
            # Unreachable
            return None

    for direction in directions:
        match direction:
            case "north":
                if (
                    (y - 1, x) != previous
                    and 0 <= y - 1
                    and map[y - 1][x] in ["|", "7", "F"]
                ):
                    return y - 1, x
            case "south":
                if (
                    (y + 1, x) != previous
                    and y + 1 < height
                    and map[y + 1][x] in ["|", "L", "J"]
                ):
                    return y + 1, x
            case "west":
                if (
                    (y, x - 1) != previous
                    and 0 <= x - 1
                    and map[y][x - 1] in ["-", "L", "F"]
                ):
                    return y, x - 1
            case "east":
                if (
                    (y, x + 1) != previous
                    and x + 1 < width
                    and map[y][x + 1] in ["-", "7", "J"]
                ):
                    return y, x + 1
            case _:
                return None

    return None


def run():
    map: list[list[str]] = []
    for line in sys.stdin:
        map.append([x for x in line.strip()])

    # Get start position

    i, j = get_start(map)
    candidates = get_candidates(map, i, j)

    for candidate in candidates:
        # Follow until we either can't continue, or the next segment is the starting position
        distance = 1
        map[i][j] = candidate

        previous = (i, j)
        current = get_next(map, previous, previous)

        while current is not None and current != (i, j):
            distance += 1
            next = get_next(map, previous, current)
            previous = current
            current = next

        if current == (i, j):
            print(distance // 2)
            break


if __name__ == "__main__":
    run()
