import sys


def kmp_search(text: str, pattern: str, table: list[int] | None = None) -> list[int]:
    """
    Gets the start indices of all matches of pattern inside text
    @param text String to search for occurrences of pattern
    @param pattern Substring to search occurrences of within text
    @param Partial match table computed by kmp_preprocess
    @return Array of match indices
    """
    if table is None:
        table = kmp_preprocess(pattern)

    result: list[int] = []
    j = 0
    k = 0

    while j < len(text):
        if pattern[k] == text[j]:
            j += 1
            k += 1
            if k == len(pattern):
                result.append(j - k)
                k = table[k]
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1

    return result


def kmp_preprocess(pattern: str) -> list[int]:
    """
    Computes partial match table for KMP algorithm
    @param pattern Pattern for which to compute partial match table
    @return Table of indices to continue search at
    """
    result = [-1] * (len(pattern) + 1)
    candidate = 0

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[candidate]:
            result[i] = result[candidate]
        else:
            result[i] = candidate
            while candidate >= 0 and pattern[i] != pattern[candidate]:
                candidate = result[candidate]
        candidate += 1

    result[-1] = candidate

    return result


def run():
    lines: list[int] = []
    patterns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tables = [kmp_preprocess(x) for x in patterns]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for line in sys.stdin:
        digits: list[tuple[int, int]] = []  # Tuples of index, value
        digits.extend([(i, int(c)) for i, c in enumerate(line) if c.isnumeric()])

        for table, value, pattern in zip(tables, values, patterns):
            digits.extend([(i, value) for i in kmp_search(line, pattern, table)])
        digits.sort()

        lines.append(digits[0][1] * 10 + digits[-1][1])

    print(sum(lines))


if __name__ == "__main__":
    run()
