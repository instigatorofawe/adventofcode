import sys


def part_a(lines: list[str]):
    result = 0
    for line in lines:
        values = [int(x) for x in line.split()]
        differences = [a - b for a, b in zip(values[1:], values[:-1])]

        result += (
            all([x < 0 for x in differences]) or all([x > 0 for x in differences])
        ) and all([abs(x) <= 3 for x in differences])

    print(result)


def part_b(lines: list[str]):
    result = 0
    for line in lines:
        values = [int(x) for x in line.split()]

        if evaluate(values):
            result += 1
        else:
            for i in range(len(values)):
                if evaluate(values, i):
                    result += 1
                    break

    print(result)


def evaluate(values: list[int], i=None):
    if i is not None:
        values = [x for j, x in enumerate(values) if j != i]

    differences = [a - b for a, b in zip(values[1:], values[:-1])]
    return (
        all([x < 0 for x in differences]) or all([x > 0 for x in differences])
    ) and all([abs(x) <= 3 for x in differences])


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
