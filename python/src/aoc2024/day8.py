import sys


def part_a(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    values: dict[str, list[tuple[int, int]]] = {}
    antinodes = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                if c in values:
                    values[c].append((i, j))
                else:
                    values[c] = [(i, j)]

    for key in values:
        n = len(values[key])
        for i in range(n - 1):
            a, b = values[key][i]
            for j in range(i + 1, n):
                c, d = values[key][j]
                di = c - a
                dj = d - b

                if 0 <= c + di < height and 0 <= d + dj < width:
                    antinodes.add((c + di, d + dj))
                if 0 <= a - di < height and 0 <= b - dj < width:
                    antinodes.add((a - di, b - dj))

    print(len(antinodes))


def part_b(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    values: dict[str, list[tuple[int, int]]] = {}
    antinodes = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                if c in values:
                    values[c].append((i, j))
                else:
                    values[c] = [(i, j)]

    for key in values:
        n = len(values[key])
        for i in range(n - 1):
            a, b = values[key][i]
            for j in range(i + 1, n):
                c, d = values[key][j]
                di = c - a
                dj = d - b

                factorization = True
                while factorization:
                    factorization = False
                    for x in [2, 3, 5, 7, 11]:
                        if di % x == 0 and dj % x == 0:
                            di /= x
                            dj /= x
                            factorization = True

                k = 0
                while 0 <= c + k * di < height and 0 <= d + k * dj < width:
                    antinodes.add((c + k * di, d + k * dj))
                    k += 1

                k = 0
                while 0 <= a - k * di < height and 0 <= b - k * dj < width:
                    antinodes.add((a - k * di, b - k * dj))
                    k += 1

    print(len(antinodes))


def run():
    lines = [[x for x in line.strip()] for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
