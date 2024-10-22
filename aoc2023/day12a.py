import sys


def count(pattern: list[str]) -> list[int]:
    result: list[int] = []
    current_count = 0

    for c in pattern:
        match c:
            case "#":
                current_count += 1
            case _:
                if current_count > 0:
                    result.append(current_count)
                current_count = 0

    if current_count > 0:
        result.append(current_count)

    return result


def eval(pattern: list[str], counts: list[int], empty: list[int]) -> int:
    current_count = count(pattern)

    # if current_count > counts:
    #     return 0

    if current_count == counts:
        # print("".join(pattern))
        return 1

    if len(empty) == 0:
        return 0

    a = pattern.copy()
    b = pattern.copy()

    a[empty[0]] = "#"
    b[empty[0]] = "."

    return eval(a, counts, empty[1:]) + eval(b, counts, empty[1:])


def run():
    result = 0
    for line in sys.stdin:
        split_line = line.split()
        pattern = [x for x in split_line[0]]
        counts = [int(x) for x in split_line[1].split(",")]
        empty = [i for i, x in enumerate(pattern) if x == "?"]

        result += eval(pattern, counts, empty)

    print(result)


if __name__ == "__main__":
    run()


def test_eval():
    # pattern = [x for x in "?###????????"]
    # counts = [3, 2, 1]
    pattern = [x for x in "?#?#?#?#?#?#?#?"]
    counts = [1, 3, 1, 6]
    empty = [i for i, x in enumerate(pattern) if x == "?"]

    # assert count(pattern) == [3]
    print(eval(pattern, counts, empty))
