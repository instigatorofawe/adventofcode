import sys


def part_a(lines: list[str]):

    lines = iter(lines)
    times = [int(x) for x in next(lines).split() if x.isnumeric()]
    distance = [int(x) for x in next(lines).split() if x.isnumeric()]

    result = 1

    for time, distance in zip(times, distance):
        i = 1
        j = time - 1

        while i * (time - i) < distance:
            i += 1

        while j * (time - j) < distance:
            j -= 1

        result *= j - i + 1

    print(result)


def part_b(lines: list[str]):
    lines = iter(lines)
    time = int("".join([x for x in next(lines) if x.isnumeric()]))
    distance = int("".join([x for x in next(lines) if x.isnumeric()]))

    lower = 1
    upper = time

    while lower < upper:
        mid = (lower + upper) // 2
        if mid * (time - mid) < distance:
            lower = mid + 1
        else:
            upper = mid

    i = lower

    lower = lower + 1
    upper = time

    while lower < upper:
        mid = (lower + upper) // 2
        if distance < mid * (time - mid):
            lower = mid + 1
        else:
            upper = mid
    j = lower - 1

    print(j - i + 1)

    pass


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
