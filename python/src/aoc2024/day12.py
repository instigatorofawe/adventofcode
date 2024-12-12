import sys


def part_a(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    unvisited = set([(i, j) for j in range(width) for i in range(height)])
    result = 0

    while unvisited:
        area = 1
        perimeter = 0
        a, b = list(unvisited)[0]
        queue = [(a, b)]
        unvisited.remove((a, b))

        while queue:
            next_level = []
            for i, j in queue:
                neighbors = ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j))
                for x, y in neighbors:
                    if (
                        x < 0
                        or x >= height
                        or y < 0
                        or y >= width
                        or lines[x][y] != lines[a][b]
                    ):
                        perimeter += 1
                    else:
                        if (x, y) in unvisited:
                            area += 1
                            next_level.append((x, y))
                            unvisited.remove((x, y))
            queue = next_level

        result += area * perimeter
    print(result)


def part_b(lines: list[str]):
    height = len(lines)
    width = len(lines[0])

    unvisited = set([(i, j) for j in range(width) for i in range(height)])
    result = 0

    while unvisited:
        area = 1
        perimeter = 0
        a, b = list(unvisited)[0]

        queue = [(a, b)]
        points = set([(a, b)])
        unvisited.remove((a, b))

        value = lines[a][b]

        while queue:
            next_level = []
            for i, j in queue:
                neighbors = ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j))
                for x, y in neighbors:
                    if (
                        x < 0
                        or x >= height
                        or y < 0
                        or y >= width
                        or lines[x][y] != lines[a][b]
                    ):
                        perimeter += 1
                    else:
                        if (x, y) in unvisited:
                            area += 1
                            next_level.append((x, y))
                            unvisited.remove((x, y))
                            points.add((x, y))
            queue = next_level

        sides = 0
        # Compute number of sides
        min_i = min([i for i, j in points])
        max_i = max([i for i, j in points])
        min_j = min([j for i, j in points])
        max_j = max([j for i, j in points])

        for i in range(min_i, max_i + 1):
            prev_upper = False
            prev_lower = False
            for j in range(min_j, max_j + 1):
                # Detect upper edges
                if (
                    (i, j) in points
                    and lines[i][j] == value
                    and (i == min_i or lines[i - 1][j] != value)
                ):
                    if prev_upper == False:
                        sides += 1
                        prev_upper = True
                else:
                    prev_upper = False
                # Detect lower edges
                if (
                    (i, j) in points
                    and lines[i][j] == value
                    and (i == max_i or lines[i + 1][j] != value)
                ):
                    if prev_lower == False:
                        sides += 1
                        prev_lower = True
                else:
                    prev_lower = False

        for j in range(min_j, max_j + 1):
            prev_left = False
            prev_right = False
            for i in range(min_i, max_i + 1):
                # Detect left edges
                if (
                    (i, j) in points
                    and lines[i][j] == value
                    and (j == min_j or lines[i][j - 1] != value)
                ):
                    if prev_left == False:
                        sides += 1
                        prev_left = True
                else:
                    prev_left = False
                # Detect right edges
                if (
                    (i, j) in points
                    and lines[i][j] == value
                    and (j == max_j or lines[i][j + 1] != value)
                ):
                    if prev_right == False:
                        sides += 1
                        prev_right = True
                else:
                    prev_right = False

        result += sides * area
        # print(f"value: {value}, area: {area}, sides: {sides}: price: {sides * area}")

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
