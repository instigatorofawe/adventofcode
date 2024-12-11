import sys


def blink(values):
    result = []
    for x in values:
        if x == 0:
            result.append(1)
        elif len(str(x)) % 2 == 0:
            s = str(x)
            l = len(s)
            result.append(int(s[: (l // 2)]))
            result.append(int(s[(l // 2) :]))
        else:
            result.append(x * 2024)
    return result


dp = {}


def blink_dp(value: int, n: int):
    if (value, n) in dp:
        return dp[(value, n)]

    if n == 1:
        result = len(blink([value]))
    else:
        result = 0
        s = blink([value])
        for x in s:
            result += blink_dp(x, n - 1)
    dp[(value, n)] = result
    return result


def part_a(lines: list[str]):
    values = [int(x) for x in lines[0].split()]
    for i in range(25):
        values = blink(values)
    print(len(values))


def part_b(lines: list[str]):
    values = [int(x) for x in lines[0].split()]
    result = 0

    for x in values:
        result += blink_dp(x, 75)
    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
