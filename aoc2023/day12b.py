import sys


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


def eval(pattern: str, counts: list[int]) -> int:
    return dp(pattern, counts, 0, 0, 0, {})


def run():
    result = 0
    for line in sys.stdin:
        split_line = line.split()
        pattern = "?".join([split_line[0] for _ in range(5)])
        counts = [int(x) for x in split_line[1].split(",")] * 5
        result += eval(pattern, counts)

    print(result)


if __name__ == "__main__":
    run()
