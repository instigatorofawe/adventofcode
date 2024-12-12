import sys


def part_a(lines: list[str]):
    result = 0
    for line in lines:
        numbers = [x for x in line if x.isnumeric()]
        result += int(numbers[0] + numbers[-1])
    print(result)


def part_b(lines: list[str]):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    result = 0
    for line in lines:
        values = []
        for i in range(len(line)):
            if line[i].isnumeric():
                values.append(int(line[i]))
            else:
                for digit in digits:
                    if line[i:].startswith(digit):
                        values.append(digits[digit])
                        break
        result += values[0] * 10 + values[-1]
    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
