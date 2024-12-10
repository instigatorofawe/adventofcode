import sys


def part_a(lines: list[str]):
    result = 0
    for line in lines:
        for i in range(len(line)):
            x = line[i:]
            if x.startswith("mul(") and ")" in x:
                exp = x[(x.index("(") + 1) : x.index(")")]
                if "," in exp:
                    s = exp.split(",")
                    if s[0].isnumeric() and s[1].isnumeric():
                        result += int(s[0]) * int(s[1])
    print(result)


def part_b(lines: list[str]):
    result = 0
    enabled = True
    for line in lines:
        for i in range(len(line)):
            x = line[i:]
            if x.startswith("do()"):
                enabled = True
            elif x.startswith("don't()"):
                enabled = False
            elif enabled and x.startswith("mul(") and ")" in x:
                exp = x[(x.index("(") + 1) : x.index(")")]
                if "," in exp:
                    s = exp.split(",")
                    if s[0].isnumeric() and s[1].isnumeric():
                        result += int(s[0]) * int(s[1])
    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
