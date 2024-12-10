import sys


def run():
    result = 0
    for line in sys.stdin:
        split_line = line.split("|")
        memo = set(
            [int(x) for x in split_line[0].split(":")[1].split(" ") if x.isnumeric()]
        )

        numbers = [int(x) for x in split_line[1].split() if x.isnumeric()]
        matches = sum([x in memo for x in numbers])

        points = 1 << (matches - 1) if matches > 0 else 0
        result += points

    print(result)


if __name__ == "__main__":
    run()
