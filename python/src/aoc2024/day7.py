import sys


def part_a(lines: list[str]):
    result = 0
    for line in lines:
        s = line.split(":")
        l = int(s[0])
        r = [int(x) for x in s[1].split()]
        n = len(r) - 1

        for j in range(2**n):
            value = r[0]
            for k in range(n):
                if (1 << k) & j > 0:
                    value *= r[k + 1]
                else:
                    value += r[k + 1]
            if value == l:
                result += value
                break
    print(result)


def part_b(lines: list[str]):
    result = 0
    for line in lines:
        s = line.split(":")
        l = int(s[0])
        r = [int(x) for x in s[1].split()]
        n = len(r) - 1

        # Build abstract syntax tree
        for j in range(3**n):
            value = r[0]
            for k in range(n):
                match (j // (3**k)) % 3:
                    case 0:
                        value += r[k + 1]
                    case 1:
                        value *= r[k + 1]
                    case 2:
                        value = int(str(value) + str(r[k + 1]))

            #
            if value == l:
                result += value
                break

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
