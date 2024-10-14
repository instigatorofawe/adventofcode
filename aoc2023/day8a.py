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

    steps = 0
    current = "AAA"

    while current != "ZZZ":
        index = 0 if instructions[steps % len(instructions)] == "L" else 1
        current = lookup[current][index]
        steps += 1

    print(steps)


if __name__ == "__main__":
    run()
