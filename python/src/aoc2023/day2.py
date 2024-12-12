import sys


def part_a(lines: list[str]):
    limits = {"red": 12, "green": 13, "blue": 14}
    result = 0

    for line in lines:
        s = line.split(":")
        id = int(s[0].split()[1])
        draws = [y.split() for x in s[1].split(";") for y in x.split(",")]

        possible = True

        for count, color in draws:
            if int(count) > limits[color]:
                possible = False
                break

        if possible:
            result += id
    print(result)


def part_b(lines: list[str]):
    result = 0
    for line in lines:
        s = line.split(":")
        draws = [y.split() for x in s[1].split(";") for y in x.split(",")]

        minimum = {"red": 0, "green": 0, "blue": 0}
        for count, color in draws:
            minimum[color] = max(minimum[color], int(count))

        prod = 1
        for val in minimum.values():
            prod *= val

        result += prod

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
