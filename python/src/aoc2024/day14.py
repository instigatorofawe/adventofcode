import sys


def display(robots, width, height):
    values = [["." for _ in range(width)] for _ in range(height)]
    for (x, y), _ in robots:
        values[y][x] = "#"
    for line in values:
        print("".join(line))


def part_a(lines: list[str]):
    width = 101
    height = 103
    # width = 11
    # height = 7

    robots = []
    for line in lines:
        s = line.split()
        p = int(s[0][2 : s[0].index(",")]), int(s[0][s[0].index(",") + 1 :])
        v = int(s[1][2 : s[1].index(",")]), int(s[1][s[1].index(",") + 1 :])
        robots.append([p, v])

    for _ in range(100):
        for i, robot in enumerate(robots):
            (x, y), (vx, vy) = robot
            x = x + vx
            y = y + vy

            if x < 0:
                x += width
            elif x >= width:
                x = x % width

            if y < 0:
                y += height
            elif y >= height:
                y = y % height
            robots[i] = (x, y), (vx, vy)

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for robot in robots:
        (x, y), _ = robot
        if x < width // 2:
            if y < height // 2:
                q1 += 1
            elif y > height // 2:
                q2 += 1
        elif x > width // 2:
            if y < height // 2:
                q3 += 1
            elif y > height // 2:
                q4 += 1

    print(q1 * q2 * q3 * q4)


def part_b(lines: list[str]):
    width = 101
    height = 103

    robots = []
    for line in lines:
        s = line.split()
        p = int(s[0][2 : s[0].index(",")]), int(s[0][s[0].index(",") + 1 :])
        v = int(s[1][2 : s[1].index(",")]), int(s[1][s[1].index(",") + 1 :])
        robots.append([p, v])
    # print(sorted([x for x, p in robots]))

    for t in range(100000):
        for i, robot in enumerate(robots):
            (x, y), (vx, vy) = robot
            x = x + vx
            y = y + vy

            if x < 0:
                x += width
            elif x >= width:
                x = x % width

            if y < 0:
                y += height
            elif y >= height:
                y = y % height
            robots[i] = (x, y), (vx, vy)

        unique = set()
        for position, _ in robots:
            unique.add(position)
        if len(unique) == len(robots):
            display(robots, width, height)
            print(t + 1)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
