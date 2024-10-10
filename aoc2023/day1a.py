import sys


def run():
    lines: list[int] = []
    for line in sys.stdin:
        numbers = [x for x in line if x.isnumeric()]
        lines.append(int(numbers[0] + numbers[-1]))
    print(sum(lines))


if __name__ == "__main__":
    run()
