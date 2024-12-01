import sys


def run():
    left = []
    right = []
    result = 0
    for line in sys.stdin:
        s = line.strip().split(" ")
        left.append(int(s[0]))
        right.append(int(s[-1]))

    left.sort()
    right.sort()

    for a, b in zip(left, right):
        result += abs(a - b)

    print(result)


if __name__ == "__main__":
    run()
