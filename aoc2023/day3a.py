import sys


def run():
    symbols = {"*", "#", "$", "+", "-", "=", "@", "&", "%", "/"}

    symbol_table: list[list[int]] = []  # row, column
    number_table: list[list[tuple[int, int, int]]] = []  # row, value, start, end

    for line in sys.stdin:
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

    # print(number_table)
    # print(symbol_table)

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


if __name__ == "__main__":
    run()
