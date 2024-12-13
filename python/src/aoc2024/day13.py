import sys


def part_a(lines: list[str]):
    l = iter(lines)
    result = 0

    while True:
        a = next(l)
        b = next(l)
        prize = next(l)
        s = next(l, None)

        a_x = int(a[a.index("X") + 2 : a.index(",")])
        a_y = int(a[a.index("Y") + 2 :])

        b_x = int(b[b.index("X") + 2 : b.index(",")])
        b_y = int(b[b.index("Y") + 2 :])

        prize_x = int(prize[prize.index("X") + 2 : prize.index(",")])
        prize_y = int(prize[prize.index("Y") + 2 :])

        i = (prize_x * b_y - prize_y * b_x) / (a_x * b_y - a_y * b_x)
        j = (prize_y * a_x - prize_x * a_y) / (a_x * b_y - a_y * b_x)
        if i == int(i) and j == int(j) and i <= 100 and j <= 100:
            result += int(3 * i + j)

        if s is None:
            break
    print(result)


def part_b(lines: list[str]):
    l = iter(lines)
    result = 0

    while True:
        a = next(l)
        b = next(l)
        prize = next(l)
        s = next(l, None)

        a_x = int(a[a.index("X") + 2 : a.index(",")])
        a_y = int(a[a.index("Y") + 2 :])

        b_x = int(b[b.index("X") + 2 : b.index(",")])
        b_y = int(b[b.index("Y") + 2 :])

        prize_x = int(prize[prize.index("X") + 2 : prize.index(",")]) + 10000000000000
        prize_y = int(prize[prize.index("Y") + 2 :]) + 10000000000000

        i = (prize_x * b_y - prize_y * b_x) / (a_x * b_y - a_y * b_x)
        j = (prize_y * a_x - prize_x * a_y) / (a_x * b_y - a_y * b_x)
        if i == int(i) and j == int(j):
            result += int(3 * i + j)

        if s is None:
            break
    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
