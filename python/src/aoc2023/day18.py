import sys


def part_a(lines: list[str]):
    dig = []
    i = 0
    j = 0

    floor = 0
    ceil = 0
    left = 0
    right = 0

    for line in lines:
        s = line.split()
        d = int(s[1])
        dig.append((s[0], d, s[2][1:-1]))
        match s[0]:
            case "L":
                j -= d
                left = min(left, j)
            case "R":
                j += d
                right = max(right, j)
            case "U":
                i -= d
                floor = min(floor, i)
            case "D":
                i += d
                ceil = max(ceil, i)

    height = ceil - floor + 1
    width = right - left + 1

    tiles = [["." for _ in range(width)] for _ in range(height)]

    i = -floor
    j = -left

    prev = None
    result = 0

    for direction, distance, _ in dig:
        match (prev, direction):
            case ("U", "L") | ("R", "D"):
                tiles[i][j] = "7"
            case ("L", "D") | ("U", "R"):
                tiles[i][j] = "F"
            case ("D", "R") | ("L", "U"):
                tiles[i][j] = "L"
            case ("R", "U") | ("D", "L"):
                tiles[i][j] = "J"

        match direction:
            case "L":
                for _ in range(distance):
                    j -= 1
                    tiles[i][j] = "-"
            case "R":
                for _ in range(distance):
                    j += 1
                    tiles[i][j] = "-"
            case "D":
                for _ in range(distance):
                    i += 1
                    tiles[i][j] = "|"
            case "U":
                for _ in range(distance):
                    i -= 1
                    tiles[i][j] = "|"

        prev = direction
        result += distance

    direction = dig[0][0]
    match (prev, direction):
        case ("U", "L") | ("R", "D"):
            tiles[i][j] = "7"
        case ("L", "D") | ("U", "R"):
            tiles[i][j] = "F"
        case ("D", "R") | ("L", "U"):
            tiles[i][j] = "L"
        case ("R", "U") | ("D", "L"):
            tiles[i][j] = "J"

    for row in tiles:
        boundary_count = 0
        stack: list[str] = []

        # print("".join(row))

        for c in row:
            match c:
                case ".":
                    if boundary_count % 2 == 1:
                        result += 1
                case "|":
                    boundary_count += 1
                case "F" | "L":
                    stack.append(c)
                case "7" | "J":
                    prev = stack.pop()
                    if (c, prev) == ("7", "L") or (c, prev) == ("J", "F"):
                        boundary_count += 1
                case _:
                    pass

    print(result)


def part_b(lines: list[str]):
    result = 0
    a, b = 0, 0

    for line in lines:
        s = line.split()
        distance = int(s[2][2:-2], 16)
        # print(distance)
        match s[2][-2]:
            case "2":
                c, d = a, b - distance
            case "0":
                c, d = a, b + distance
            case "3":
                c, d = a - distance, b
            case "1":
                c, d = a + distance, b

        # Shoelace formula
        result += (b * c - a * d) + distance
        a, b = c, d

    print(result // 2 + 1)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
