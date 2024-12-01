import sys


def run():
    left = []
    right = []
    result = 0
    for line in sys.stdin:
        s = line.strip().split(" ")
        left.append(int(s[0]))
        right.append(int(s[-1]))

    counts = {}
    for r in right:
        counts[r] = counts.get(r, 0) + 1

    for l in left:
        result += counts.get(l, 0) * l

    print(result)


if __name__ == "__main__":
    run()
