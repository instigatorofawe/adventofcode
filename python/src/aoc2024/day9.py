import sys


def part_a(lines: list[str]):
    values = [int(x) for x in lines[0]]
    total = sum(values)
    data = [None] * total

    index = 0
    group = 0
    for i, x in enumerate(values):
        if i % 2 == 0:
            for j in range(x):
                data[index] = group
                index += 1
        else:
            index += x
            group += 1

    i = 0
    j = total - 1

    while i < j:
        if data[i] is not None or data[j] is None:
            while data[i] is not None:
                i += 1
            while data[j] is None:
                j -= 1
        else:
            data[i] = data[j]
            data[j] = None
            i += 1
            j -= 1

    result = 0
    for i, x in enumerate(data):
        if x is not None:
            result += i * x
    print(result)


def part_b(lines: list[str]):
    values = [int(x) for x in lines[0]]

    data = []
    spaces = []

    index = 0
    group = 0

    for i, x in enumerate(values):
        if i % 2 == 0:
            data.append((index, group, x))
            index += x
        else:
            spaces.append((index, x))
            index += x
            group += 1

    for j in range(len(data) - 1, -1, -1):
        start, group, length = data[j]
        for i, (index, empty_length) in enumerate(spaces):
            if index > start:
                break
            if length <= empty_length:
                data[j] = (index, group, length)
                spaces[i] = (index + length, empty_length - length)
                break

    result = 0
    for start, group, length in data:
        for i in range(length):
            result += group * (start + i)
    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
