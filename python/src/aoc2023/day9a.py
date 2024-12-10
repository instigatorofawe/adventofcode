import sys


def extrapolate(arr: list[int]):
    stack = [arr]
    while any([x != 0 for x in stack[-1]]):
        stack.append([y - x for x, y in zip(stack[-1][:-1], stack[-1][1:])])

    current = stack.pop()[-1]

    while stack:
        current += stack.pop()[-1]

    return current


def run():
    result: int = 0
    for line in sys.stdin:
        result += extrapolate([int(x) for x in line.split()])

    print(result)


if __name__ == "__main__":
    run()
