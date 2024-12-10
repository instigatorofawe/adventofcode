import sys


def part_a(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    trailheads = []
    for i in range(height):
        for j in range(width):
            if lines[i][j] == 0:
                trailheads.append((i, j))
    result = 0

    for i, j in trailheads:
        queue = [(i, j)]
        visited = [[False] * width for _ in range(height)]
        while queue:
            next_level = []
            for a, b in queue:
                if lines[a][b] == 9:
                    result += 1
                for x, y in ((a, b + 1), (a, b - 1), (a + 1, b), (a - 1, b)):
                    if (
                        0 <= x < height
                        and 0 <= y < width
                        and lines[x][y] == lines[a][b] + 1
                        and not visited[x][y]
                    ):
                        next_level.append((x, y))
                        visited[x][y] = True
            queue = next_level
    print(result)


def part_b(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    trailheads = []
    for i in range(height):
        for j in range(width):
            if lines[i][j] == 0:
                trailheads.append((i, j))
    result = 0

    for i, j in trailheads:
        queue = [(i, j)]
        while queue:
            next_level = []
            for a, b in queue:
                if lines[a][b] == 9:
                    result += 1
                for x, y in ((a, b + 1), (a, b - 1), (a + 1, b), (a - 1, b)):
                    if (
                        0 <= x < height
                        and 0 <= y < width
                        and lines[x][y] == lines[a][b] + 1
                        # and not visited[x][y]
                    ):
                        next_level.append((x, y))
                        # visited[x][y] = True
            queue = next_level
    print(result)


def run():
    lines = [[int(x) for x in line.strip()] for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
