import sys


def part_a(lines: list[str]):
    result = 0
    for line in lines:
        split_line = line.split("|")
        memo = set(
            [int(x) for x in split_line[0].split(":")[1].split(" ") if x.isnumeric()]
        )

        numbers = [int(x) for x in split_line[1].split() if x.isnumeric()]
        matches = sum([x in memo for x in numbers])

        points = 1 << (matches - 1) if matches > 0 else 0
        result += points

    print(result)


def part_b(lines: list[str]):
    n_matches: list[int] = []
    n_cards: dict[int, int] = {}

    for line in lines:
        split_line = line.split("|")
        memo = set(
            [int(x) for x in split_line[0].split(":")[1].split(" ") if x.isnumeric()]
        )

        numbers = [int(x) for x in split_line[1].split() if x.isnumeric()]
        matches = sum([x in memo for x in numbers])
        n_matches.append(matches)

    def dp(index: int) -> int:
        if index in n_cards:
            return n_cards[index]
        result = 1
        for i in range(n_matches[index]):
            result += dp(index + i + 1)
        n_cards[index] = result
        return result

    result = 0
    for i in range(len(n_matches) - 1, -1, -1):
        result += dp(i)

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
