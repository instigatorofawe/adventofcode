import sys


def run():
    data: list[list[str]] = []
    for line in sys.stdin:
        data.append([x for x in line])

    height = len(data)
    width = len(data[0])

    stars: list[tuple[int, int]] = []
    empty_rows = set(list(range(height)))
    empty_cols = set(list(range(width)))

    for i in range(height):
        for j in range(width):
            if data[i][j] == "#":
                stars.append((i, j))

                if i in empty_rows:
                    empty_rows.remove(i)
                if j in empty_cols:
                    empty_cols.remove(j)

    total_distances = 0
    for i in range(len(stars)):
        for j in range(i, len(stars)):
            min_y = min(stars[i][0], stars[j][0])
            max_y = max(stars[i][0], stars[j][0])
            min_x = min(stars[i][1], stars[j][1])
            max_x = max(stars[i][1], stars[j][1])

            distances = max_y - min_y + max_x - min_x
            for y in empty_rows:
                if min_y < y < max_y:
                    distances += 1
            for x in empty_cols:
                if min_x < x < max_x:
                    distances += 1

            total_distances += distances

    print(total_distances)


if __name__ == "__main__":
    run()
