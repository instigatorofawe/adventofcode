import sys


def is_hreflect(block, index) -> int:
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


def is_vreflect(block, index) -> int:
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


def hreflect(block) -> int:
    for i in range(len(block) - 1):
        if is_hreflect(block, i) == 1:
            return i + 1
    return 0


def vreflect(block) -> int:
    for i in range(len(block[0]) - 1):
        if is_vreflect(block, i) == 1:
            return i + 1
    return 0


def run():
    blocks = []

    current_block = []

    for line in sys.stdin:
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


if __name__ == "__main__":
    run()
