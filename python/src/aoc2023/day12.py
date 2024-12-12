import sys


def eval(
    pattern: str, counts: list[int], memo: dict[tuple[str, tuple[int, ...]], int]
) -> int:

    if (pattern, tuple(counts)) in memo:
        return memo[(pattern, tuple(counts))]

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

                return eval(
                    "".join(a)[pattern_start:], counts[count_index:], memo
                ) + eval("".join(b)[pattern_start:], counts[count_index:], memo)

    result: int = (current_count == 0 and count_index == len(counts)) or (
        count_index == len(counts) - 1 and current_count == counts[-1]
    )
    memo[(pattern, tuple(counts))] = result
    return result


def dp(
    pattern: str,
    counts: list[int],
    i: int,  # Character index
    j: int,  # Count index
    k: int,  # Current count
    memo: dict[tuple[int, int, int], int],
) -> int:
    if (i, j, k) in memo:
        return memo[(i, j, k)]

    if i == len(pattern):
        result: int = (j == len(counts) and k == 0) or (
            j == len(counts) - 1 and k == counts[j]
        )
        memo[(i, j, k)] = result
        return result

    if (
        j > len(counts)
        or (j == len(counts) and k > 0)
        or (j < len(counts) and k > counts[j])
    ):
        memo[(i, j, k)] = 0
        return 0

    match pattern[i]:
        case ".":
            if k > 0:
                if k != counts[j]:
                    result = 0
                else:
                    result = dp(pattern, counts, i + 1, j + 1, 0, memo)
            else:
                result = dp(pattern, counts, i + 1, j, 0, memo)

            memo[(i, j, k)] = result
            return result

        case "#":
            result = dp(pattern, counts, i + 1, j, k + 1, memo)
            memo[(i, j, k)] = result
            return result

        case _:
            # case ?

            if k > 0:
                if k == counts[j]:
                    result = dp(pattern, counts, i + 1, j + 1, 0, memo)
                else:
                    result = dp(pattern, counts, i + 1, j, k + 1, memo)

                memo[(i, j, k)] = result
                return result

            else:
                result = dp(pattern, counts, i + 1, j, 0, memo) + dp(
                    pattern, counts, i + 1, j, 1, memo
                )
                memo[(i, j, k)] = result
                return result


def part_a(lines: list[str]):
    result = 0
    memo: dict[tuple[str, tuple[int, ...]], int] = {}
    for line in lines:
        split_line = line.split()
        counts = [int(x) for x in split_line[1].split(",")]

        result += eval(split_line[0], counts, memo)
    print(result)


def part_b(lines: list[str]):
    result = 0
    for line in lines:
        split_line = line.split()
        pattern = "?".join([split_line[0] for _ in range(5)])
        counts = [int(x) for x in split_line[1].split(",")] * 5
        result += dp(pattern, counts, 0, 0, 0, {})

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
