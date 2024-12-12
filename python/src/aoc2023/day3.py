import sys


def part_a(lines: list[str]):
    symbols = {"*", "#", "$", "+", "-", "=", "@", "&", "%", "/"}

    symbol_table: list[list[int]] = []  # row, column
    number_table: list[list[tuple[int, int, int]]] = []  # row, value, start, end

    for line in lines:
        current_symbols: list[int] = []
        current_numbers: list[tuple[int, int, int]] = []

        current_start: None | int = None
        current_value = 0

        for i, c in enumerate(line):
            if c.isnumeric():
                if current_start is None:
                    current_start = i
                current_value = current_value * 10 + int(c)
            else:
                if current_start is not None:
                    current_numbers.append((current_value, current_start, i - 1))
                    current_start = None
                    current_value = 0
                if c in symbols:
                    current_symbols.append(i)

        if current_start is not None:
            current_numbers.append((current_value, current_start, len(line) - 1))

        symbol_table.append(current_symbols)
        number_table.append(current_numbers)

    total = 0

    for i, number_row in enumerate(number_table):
        if i == 0:
            symbol_indices = [
                x for y in [symbol_table[i], symbol_table[i + 1]] for x in y
            ]
        elif i == len(number_table) - 1:
            symbol_indices = [
                x for y in [symbol_table[i - 1], symbol_table[i]] for x in y
            ]
        else:
            symbol_indices = [
                x
                for y in [symbol_table[i - 1], symbol_table[i], symbol_table[i + 1]]
                for x in y
            ]

        for value, start, end in number_row:
            if any([start - 1 <= x <= end + 1 for x in symbol_indices]):
                total += value

    print(total)


def part_b(lines: list[str]):

    symbols = {"*"}

    symbol_table: list[list[int]] = []  # row, column
    number_table: list[list[tuple[int, int, int]]] = []  # row, value, start, end
    gears: dict[tuple[int, int], list[int]] = {}

    for row, line in enumerate(lines):
        current_symbols: list[int] = []
        current_numbers: list[tuple[int, int, int]] = []

        current_start: None | int = None
        current_value = 0

        for i, c in enumerate(line):
            if c.isnumeric():
                if current_start is None:
                    current_start = i
                current_value = current_value * 10 + int(c)
            else:
                if current_start is not None:
                    current_numbers.append((current_value, current_start, i - 1))
                    current_start = None
                    current_value = 0
                if c in symbols:
                    current_symbols.append(i)
                    gears[(row, i)] = []

        if current_start is not None:
            current_numbers.append((current_value, current_start, len(line) - 1))

        symbol_table.append(current_symbols)
        number_table.append(current_numbers)

    for i, number_row in enumerate(number_table):
        for value, start, end in number_row:
            if i > 0:
                for j in symbol_table[i - 1]:
                    if start - 1 <= j <= end + 1:
                        gears[(i - 1, j)].append(value)
            if i < len(number_table) - 1:

                for j in symbol_table[i + 1]:
                    if start - 1 <= j <= end + 1:
                        gears[(i + 1, j)].append(value)

            for j in symbol_table[i]:
                if start - 1 <= j <= end + 1:
                    gears[(i, j)].append(value)

    valid_gears = [x for x in gears.values() if len(x) == 2]

    total = 0
    for a, b in valid_gears:
        total += a * b

    print(total)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
