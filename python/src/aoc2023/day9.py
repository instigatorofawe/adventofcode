import sys


def extrapolate(arr: list[int]):
    stack = [arr]
    while any([x != 0 for x in stack[-1]]):
        stack.append([y - x for x, y in zip(stack[-1][:-1], stack[-1][1:])])

    current = stack.pop()[-1]

    while stack:
        current += stack.pop()[-1]

    return current


def extrapolate_b(arr: list[int]):
    stack = [arr]
    while any([x != 0 for x in stack[-1]]):
        stack.append([y - x for x, y in zip(stack[-1][:-1], stack[-1][1:])])

    current = stack.pop()[0]

    while stack:
        current = stack.pop()[0] - current

    return current


def part_a(lines: list[str]):
    result: int = 0
    for line in lines:
        result += extrapolate([int(x) for x in line.split()])

    print(result)


def part_b(lines: list[str]):
    result: int = 0
    for line in lines:
        result += extrapolate_b([int(x) for x in line.split()])

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
