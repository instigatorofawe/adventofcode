import sys


def eval(pattern: str, counts: list[int]) -> int:
    # print()
    # print(pattern)
    # print(counts)

    pattern_start = 0
    current_count = 0
    count_index = 0

    for i, c in enumerate(pattern):
        match c:
            case "#":
                current_count += 1
                if count_index >= len(counts) or current_count > counts[count_index]:
                    return 0
            case ".":
                pattern_start = i + 1
                if current_count > 0:

                    if current_count < counts[count_index]:
                        return 0

                    current_count = 0
                    count_index += 1
            case _:
                a = [x for x in pattern]
                a[i] = "."
                b = [x for x in pattern]
                b[i] = "#"

                return eval("".join(a)[pattern_start:], counts[count_index:]) + eval(
                    "".join(b)[pattern_start:], counts[count_index:]
                )

    return (current_count == 0 and count_index == len(counts)) or (
        count_index == len(counts) - 1 and current_count == counts[-1]
    )


def run():
    result = 0
    for line in sys.stdin:
        split_line = line.split()
        counts = [int(x) for x in split_line[1].split(",")]

        result += eval(split_line[0], counts)
    print(result)


if __name__ == "__main__":
    run()


def test_eval():
    result = eval("?###????????", [3, 2, 1])
    print(result)
