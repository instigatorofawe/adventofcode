import sys


def part_a(lines: list[str]):
    card_ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    hands: list[tuple[tuple[int, ...], tuple[int, ...], int]] = (
        []
    )  # Multiplicity, ranks, bid

    for line in lines:
        s = line.split()
        bid = int(s[1])
        ranks = tuple([card_ranks[x] for x in s[0]])

        hand_cards: dict[int, int] = {}
        for r in ranks:
            hand_cards[r] = hand_cards.get(r, 0) + 1

        multiplicity = tuple(sorted(hand_cards.values(), reverse=True))

        hands.append((multiplicity, ranks, bid))

    hands.sort()

    result = 0

    for i, hand in enumerate(hands):
        result += (i + 1) * hand[2]

    print(result)
    pass


def part_b(lines: list[str]):
    card_ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": -1,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    hands: list[tuple[tuple[int, ...], tuple[int, ...], int]] = (
        []
    )  # Multiplicity, ranks, bid

    for line in lines:
        s = line.split()
        bid = int(s[1])
        ranks = tuple([card_ranks[x] for x in s[0]])

        hand_cards: dict[int, int] = {}
        jokers = 0
        for r in ranks:
            if r == -1:
                jokers += 1
            else:
                hand_cards[r] = hand_cards.get(r, 0) + 1

        multiplicity = sorted(hand_cards.values(), reverse=True) if hand_cards else [0]
        multiplicity[0] += jokers

        hands.append((tuple(multiplicity), ranks, bid))

    hands.sort()

    result = 0

    for i, hand in enumerate(hands):
        result += (i + 1) * hand[2]

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
