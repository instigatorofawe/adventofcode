import sys


def run():

    lines = iter(sys.stdin)
    times = [int(x) for x in next(lines).split() if x.isnumeric()]
    distance = [int(x) for x in next(lines).split() if x.isnumeric()]

    result = 1

    for time, distance in zip(times, distance):
        i = 1
        j = time - 1

        while i * (time - i) < distance:
            i += 1

        while j * (time - j) < distance:
            j -= 1

        result *= j - i + 1

    print(result)


if __name__ == "__main__":
    run()
