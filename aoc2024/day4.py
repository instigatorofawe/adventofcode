import sys


def part_a(lines: list[str]):
    result = 0
    height = len(lines)
    width = len(lines[0])

    for i in range(height):
        for j in range(width):
            if i <= height - 4:
                vertical = "".join(
                    [lines[i][j], lines[i + 1][j], lines[i + 2][j], lines[i + 3][j]]
                )
                result += vertical == "XMAS"
                result += vertical == "SAMX"

                if j <= width - 4:
                    diag_1 = "".join(
                        [
                            lines[i][j + 3],
                            lines[i + 1][j + 2],
                            lines[i + 2][j + 1],
                            lines[i + 3][j],
                        ]
                    )
                    result += diag_1 == "XMAS"
                    result += diag_1 == "SAMX"

                    diag_2 = "".join(
                        [
                            lines[i][j],
                            lines[i + 1][j + 1],
                            lines[i + 2][j + 2],
                            lines[i + 3][j + 3],
                        ]
                    )
                    result += diag_2 == "XMAS"
                    result += diag_2 == "SAMX"
            if j <= width - 4:
                result += lines[i][j : (j + 4)] == "XMAS"
                result += lines[i][j : (j + 4)] == "SAMX"

    print(result)


def part_b(lines: list[str]):
    result = 0
    height = len(lines)
    width = len(lines[0])

    for i in range(height):
        for j in range(width):
            if i <= height - 3 and j <= width - 3:
                diag1 = "".join((lines[i][j], lines[i + 1][j + 1], lines[i + 2][j + 2]))
                diag2 = "".join((lines[i][j + 2], lines[i + 1][j + 1], lines[i + 2][j]))

                result += diag1 in ("SAM", "MAS") and diag2 in ("SAM", "MAS")
    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
