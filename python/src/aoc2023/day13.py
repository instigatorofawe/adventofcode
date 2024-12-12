import sys


def is_hreflect(block, index) -> bool:
    i = index
    j = index + 1

    while i >= 0 and j < len(block):
        for k in range(len(block[i])):
            if block[i][k] != block[j][k]:
                return False

        i -= 1
        j += 1
    return True


def is_vreflect(block, index) -> bool:
    i = index
    j = index + 1

    while i >= 0 and j < len(block[0]):
        for k in range(len(block)):
            if block[k][i] != block[k][j]:
                return False

        i -= 1
        j += 1
    return True


def hreflect(block) -> int:
    for i in range(len(block) - 1):
        if is_hreflect(block, i):
            return i + 1
    return 0


def vreflect(block) -> int:
    for i in range(len(block[0]) - 1):
        if is_vreflect(block, i):
            return i + 1
    return 0


def is_hreflect_b(block, index) -> int:
    i = index
    j = index + 1
    result = 0

    while i >= 0 and j < len(block):
        for k in range(len(block[i])):
            if block[i][k] != block[j][k]:
                result += 1

        i -= 1
        j += 1
    return result


def is_vreflect_b(block, index) -> int:
    i = index
    j = index + 1
    result = 0

    while i >= 0 and j < len(block[0]):
        for k in range(len(block)):
            if block[k][i] != block[k][j]:
                result += 1

        i -= 1
        j += 1
    return result


def hreflect_b(block) -> int:
    for i in range(len(block) - 1):
        if is_hreflect_b(block, i):
            return i + 1
    return 0


def vreflect_b(block) -> int:
    for i in range(len(block[0]) - 1):
        if is_vreflect_b(block, i):
            return i + 1
    return 0


def part_a(lines: list[str]):
    blocks = []

    current_block = []

    for line in lines:
        if line.isspace():
            blocks.append(current_block)
            current_block = []
        else:
            current_block.append(line.strip())
    blocks.append(current_block)

    result = 0
    for block in blocks:
        result += vreflect(block)
        result += 100 * hreflect(block)
    print(result)


def part_b(lines: list[str]):
    blocks = []

    current_block = []

    for line in lines:
        if line.isspace():
            blocks.append(current_block)
            current_block = []
        else:
            current_block.append(line.strip())
    blocks.append(current_block)

    result = 0
    for block in blocks:
        result += vreflect_b(block)
        result += 100 * hreflect_b(block)
    print(result)


def run():
    lines = [line for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
