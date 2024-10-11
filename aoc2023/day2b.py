import sys


def run():
    power_sum = 0
    for line in sys.stdin:
        split_line = line.split(":")
        draws = [
            [y.strip().split(" ") for y in x.split(",")]
            for x in split_line[1].split(";")
        ]
        draws_flat = [x for y in draws for x in y]

        minimum = {"red": 0, "green": 0, "blue": 0}
        for count, color in draws_flat:
            minimum[color] = max(minimum[color], int(count))

        prod = 1
        for val in minimum.values():
            prod *= val

        power_sum += prod

    print(power_sum)


if __name__ == "__main__":
    run()
