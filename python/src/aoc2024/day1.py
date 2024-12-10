import sys


def part_a(lines: list[str]):
    left = []
    right = []

    for line in lines:
        s = line.strip().split()
        left.append(int(s[0]))
        right.append(int(s[1]))

    left.sort()
    right.sort()

    result = 0

    for a, b in zip(left, right):
        result += abs(a - b)

    print(result)


def part_b(lines: list[str]):
    left = []
    right = {}

    for line in lines:
        s = line.strip().split()
        left.append(int(s[0]))

        r = int(s[1])
        right[r] = right.get(r, 0) + 1

    result = 0
    for l in left:
        result += l * right.get(l, 0)

    print(result)


def run():
    lines = [line for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
