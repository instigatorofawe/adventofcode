import sys


def run():
    limits = {"red": 12, "green": 13, "blue": 14}

    possible_ids = 0
    for line in sys.stdin:
        split_line = line.split(":")
        game_id = int(split_line[0].split(" ")[1])
        draws = [
            [y.strip().split(" ") for y in x.split(",")]
            for x in split_line[1].split(";")
        ]
        draws_flat = [x for y in draws for x in y]
        possible = True

        for count, color in draws_flat:
            if int(count) > limits[color]:
                possible = False
                break

        if possible:
            possible_ids += game_id

    print(possible_ids)


if __name__ == "__main__":

    run()
