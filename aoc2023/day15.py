import sys

def hash(x: str) -> int:
    value = 0
    for c in x:
        value += ord(c)
        value = value * 17
        value = value % 256
    return value

def part_a(lines: list[str]):
    items = lines[0].split(",")
    result = 0

    for item in items:
        result += hash(item)

    print(result)


def part_b(lines: list[str]):
    items = lines[0].split(",")
    result = 0
    boxes = [[] for _ in range(256)]

    for item in items:
        if "=" in item:
            s = item.split("=")
            label = s[0]
            lens = int(s[1])
            index = hash(label)

            matched = False

            for i, x in enumerate(boxes[index]):
                if x[0] == label:
                    boxes[index][i] = (label, lens)
                    matched = True
                    break
            if not matched:
                boxes[index].append((label, lens))

        elif "-" in item:
            s = item.split("-")
            label = s[0]
            index = hash(label)
            for i, x in enumerate(boxes[index]):
                if x[0] == label:
                    del boxes[index][i]
                    break
    for i, box in enumerate(boxes):
        if box:
            for j, x in enumerate(box):
                result += (1+i) * (1+j) * x[1]
    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
