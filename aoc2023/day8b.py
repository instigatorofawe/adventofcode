import math
import sys


def run():
    lines = iter(sys.stdin)
    instructions = next(lines).strip()
    _ = next(lines)

    lookup: dict[str, list[str]] = {}
    while True:
        current_line = next(lines, None)
        if current_line is None:
            break

        split_line = current_line.split("=")

        key = split_line[0].strip()
        values = split_line[1].split(",")
        left = values[0]
        left = left[left.find("(") + 1 :]

        right = values[1]
        right = right[1 : right.find(")")]

        lookup[key] = [left, right]

    starts = [x for x in lookup.keys() if x[-1] == "A"]
    results: list[int] = []

    for current in starts:
        steps = 0

        while current[-1] != "Z":
            index = 0 if instructions[steps % len(instructions)] == "L" else 1
            current = lookup[current][index]
            steps += 1
        results.append(steps)

    print(math.lcm(*results))


if __name__ == "__main__":
    run()
