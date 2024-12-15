import sys


def get_pos(layout: list[list[str]]) -> tuple[int, int]:
    for i, line in enumerate(layout):
        for j, c in enumerate(line):
            if c == "@":
                return i, j
    return -1, -1


def do_move(layout, i, j, m) -> tuple[int, int]:
    height = len(layout)
    width = len(layout[0])
    match m:
        case ">":
            # scan until . or #
            for x in range(j + 1, width):
                if layout[i][x] == "#":
                    return i, j
                elif layout[i][x] == ".":
                    layout[i][j] = "."
                    layout[i][j + 1] = "@"
                    for y in range(j + 2, x + 1):
                        layout[i][y] = "O"
                    return i, j + 1
        case "<":
            for x in range(j - 1, 0, -1):
                if layout[i][x] == "#":
                    return i, j
                elif layout[i][x] == ".":
                    layout[i][j] = "."
                    layout[i][j - 1] = "@"
                    for y in range(j - 2, x - 1, -1):
                        layout[i][y] = "O"
                    return i, j - 1
        case "^":
            for x in range(i - 1, 0, -1):
                if layout[x][j] == "#":
                    return i, j
                elif layout[x][j] == ".":
                    layout[i][j] = "."
                    layout[i - 1][j] = "@"
                    for y in range(i - 2, x - 1, -1):
                        layout[y][j] = "O"
                    return i - 1, j
        case "v":
            for x in range(i + 1, height):
                if layout[x][j] == "#":
                    return i, j
                elif layout[x][j] == ".":
                    layout[i][j] = "."
                    layout[i + 1][j] = "@"
                    for y in range(i + 2, x + 1):
                        layout[y][j] = "O"
                    return i + 1, j
    return i, j


def part_a(lines: list[str]):
    mode = "layout"
    layout: list[list[str]] = []
    moves = ""
    for line in lines:
        if len(line) == 0:
            mode = ""
        elif mode == "layout":
            layout.append([c for c in line])
        else:
            moves = moves + line

    i, j = get_pos(layout)

    for m in moves:
        i, j = do_move(layout, i, j, m)

    result = 0

    for x, line in enumerate(layout):
        for y, c in enumerate(line):
            if c == "O":
                result += 100 * x + y

    print(result)


def do_move_b(layout, i, j, m):
    height = len(layout)
    width = len(layout[0])
    match m:
        case ">":
            # scan until . or #
            buffer = []
            for x in range(j + 1, width):
                if layout[i][x] == "#":
                    return i, j
                elif layout[i][x] == ".":
                    layout[i][j] = "."
                    layout[i][j + 1] = "@"
                    for z, y in enumerate(range(j + 2, x + 1)):
                        layout[i][y] = buffer[z]
                    return i, j + 1
                else:
                    buffer.append(layout[i][x])
        case "<":
            buffer = []
            for x in range(j - 1, 0, -1):
                if layout[i][x] == "#":
                    return i, j
                elif layout[i][x] == ".":
                    layout[i][j] = "."
                    layout[i][j - 1] = "@"
                    for z, y in enumerate(range(j - 2, x - 1, -1)):
                        layout[i][y] = buffer[z]
                    return i, j - 1
                else:
                    buffer.append(layout[i][x])
        case "^":
            contact = set([(i, j)])
            scan = set([j])
            for x in range(i - 1, 0, -1):
                if not scan:
                    break
                next_level = set()
                for y in scan:
                    match layout[x][y]:
                        case "#":
                            return i, j
                        case "]":
                            contact.add((x, y))
                            contact.add((x, y - 1))
                            next_level.add(y)
                            next_level.add(y - 1)
                        case "[":
                            contact.add((x, y))
                            contact.add((x, y + 1))
                            next_level.add(y)
                            next_level.add(y + 1)

                scan = next_level

            for a, b in contact:
                if layout[a - 1][b] == "#":
                    return i, j

            coordinates = list(contact)
            values = [layout[a][b] for a, b in coordinates]
            for a, b in coordinates:
                layout[a][b] = "."
            for x, (a, b) in zip(values, coordinates):
                layout[a - 1][b] = x

            return i - 1, j

        case "v":
            contact = set([(i, j)])
            scan = set([j])
            for x in range(i + 1, height):
                if not scan:
                    break
                next_level = set()
                for y in scan:
                    match layout[x][y]:
                        case "#":
                            return i, j
                        case "]":
                            contact.add((x, y))
                            contact.add((x, y - 1))
                            next_level.add(y)
                            next_level.add(y - 1)
                        case "[":
                            contact.add((x, y))
                            contact.add((x, y + 1))
                            next_level.add(y)
                            next_level.add(y + 1)

                scan = next_level

            for a, b in contact:
                if layout[a + 1][b] == "#":
                    return i, j

            coordinates = list(contact)
            values = [layout[a][b] for a, b in coordinates]
            for a, b in coordinates:
                layout[a][b] = "."
            for x, (a, b) in zip(values, coordinates):
                layout[a + 1][b] = x

            return i + 1, j
    return i, j


def expand(line):
    result = []
    for c in line:
        match c:
            case "#":
                result.append("#")
                result.append("#")
            case "O":
                result.append("[")
                result.append("]")
            case ".":
                result.append(".")
                result.append(".")
            case "@":
                result.append("@")
                result.append(".")
    return result


def part_b(lines: list[str]):
    mode = "layout"
    layout: list[list[str]] = []
    moves = ""
    for line in lines:
        if len(line) == 0:
            mode = ""
        elif mode == "layout":
            layout.append(expand(line))
        else:
            moves = moves + line

    i, j = get_pos(layout)

    # for line in layout:
    #     print("".join(line))

    for m in moves:
        i, j = do_move_b(layout, i, j, m)
        # print(f"move: {m}; {i}, {j}")
        #
        # for line in layout:
        #     print("".join(line))

    result = 0

    for x, line in enumerate(layout):
        for y, c in enumerate(line):
            if c == "[":
                result += 100 * x + y

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
