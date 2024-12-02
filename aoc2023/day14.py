import sys


def part_a(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    heights = [height] * width
    result = 0

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            match c:
                case "O":
                    result += heights[j]
                    heights[j] -= 1
                case "#":
                    heights[j] = height - i - 1
                case _:
                    pass
    print(result)


def load(lines: list[str]):
    height = len(lines)
    width = len(lines[0])
    result = 0

    for i in range(height):
        for j in range(width):
            if lines[i][j] == "O":
                result += height - i

    return result


def part_b(lines: list[str]):
    N_CYCLES = 1_000_000_000

    height = len(lines)
    width = len(lines[0])

    board_list: list[list[str]] = [lines]
    board_map: dict[str, int] = {"".join(lines): 0}

    # Cycle detection

    for i in range(1, N_CYCLES + 1):
        lines = cycle(lines)
        if "".join(lines) in board_map:
            cycle_start = board_map["".join(lines)]
            cycle_duration = i - cycle_start
            index = cycle_start + (N_CYCLES - i) % cycle_duration
            print(load(board_list[index]))
            break

        else:
            board_list.append(lines)
            board_map["".join(lines)] = i


def cycle(lines: list[str]) -> list[str]:
    lines = north(lines)
    lines = west(lines)
    lines = south(lines)
    lines = east(lines)

    return lines


def north(lines: list[str]) -> list[str]:
    height = len(lines)
    width = len(lines[0])

    result = [["."] * width for _ in range(height)]
    heights = [0] * width

    for i in range(height):
        for j in range(width):
            match lines[i][j]:
                case "O":
                    result[heights[j]][j] = "O"
                    heights[j] += 1
                case "#":
                    result[i][j] = "#"
                    heights[j] = i + 1

    return ["".join(x) for x in result]


def south(lines: list[str]) -> list[str]:
    height = len(lines)
    width = len(lines[0])

    result = [["."] * width for _ in range(height)]
    heights = [height - 1] * width

    for i in range(height - 1, -1, -1):
        for j in range(width):
            match lines[i][j]:
                case "O":
                    result[heights[j]][j] = "O"
                    heights[j] -= 1
                case "#":
                    result[i][j] = "#"
                    heights[j] = i - 1
    return ["".join(x) for x in result]


def east(lines: list[str]) -> list[str]:
    height = len(lines)
    width = len(lines[0])

    result = [["."] * width for _ in range(height)]
    widths = [width - 1] * height

    for j in range(width - 1, -1, -1):
        for i in range(height):
            match lines[i][j]:
                case "O":
                    result[i][widths[i]] = "O"
                    widths[i] -= 1
                case "#":
                    result[i][j] = "#"
                    widths[i] = j - 1

    return ["".join(x) for x in result]


def west(lines: list[str]) -> list[str]:
    height = len(lines)
    width = len(lines[0])

    result = [["."] * width for _ in range(height)]
    widths = [0] * height

    for j in range(width):
        for i in range(height):
            match lines[i][j]:
                case "O":
                    result[i][widths[i]] = "O"
                    widths[i] += 1
                case "#":
                    result[i][j] = "#"
                    widths[i] = j + 1

    return ["".join(x) for x in result]


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
