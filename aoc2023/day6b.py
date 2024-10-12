import sys


def run():

    lines = iter(sys.stdin)
    time = int("".join([x for x in next(lines) if x.isnumeric()]))
    distance = int("".join([x for x in next(lines) if x.isnumeric()]))

    lower = 1
    upper = time

    while lower < upper:
        mid = (lower + upper) // 2
        if mid * (time - mid) < distance:
            lower = mid + 1
        else:
            upper = mid

    i = lower

    lower = lower + 1
    upper = time

    while lower < upper:
        mid = (lower + upper) // 2
        if distance < mid * (time - mid):
            lower = mid + 1
        else:
            upper = mid
    j = lower - 1

    print(j - i + 1)


if __name__ == "__main__":
    run()
