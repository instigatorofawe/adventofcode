import sys


def part_a(lines: list[str]):
    result = 0
    rules = True
    orders = []
    for line in lines:
        if rules:
            if len(line) == 0:
                rules = False
            else:
                s = line.split("|")
                left = int(s[0])
                right = int(s[1])
                orders.append((left, right))
        else:
            values = [int(x) for x in line.split(",")]
            line = {}
            valid = True
            for i, value in enumerate(values):
                line[value] = i
            for a, b in orders:
                if a in line and b in line and line[a] > line[b]:
                    valid = False
                    break

            if valid:
                result += values[len(values) // 2]

    print(result)


def part_b(lines: list[str]):
    result = 0
    rules = True
    orders = {}

    for line in lines:
        if rules:
            if len(line) == 0:
                rules = False
            else:
                s = line.split("|")
                left = int(s[0])
                right = int(s[1])

                if left in orders:
                    orders[left].add(right)
                else:
                    orders[left] = set([right])
        else:
            values = [int(x) for x in line.split(",")]
            indices = {}
            valid = True
            for i, value in enumerate(values):
                indices[value] = i

            for x in values:
                if x in orders:
                    for y in orders[x]:
                        if y in indices and indices[x] > indices[y]:
                            valid = False
                            break

            if not valid:
                # Toposort
                visited = [False] * len(values)
                sorted = []
                stack = []

                # print(len(visited))

                def traverse(i):
                    nonlocal stack
                    nonlocal values
                    nonlocal visited
                    nonlocal indices

                    if not visited[i]:
                        visited[i] = True
                        if values[i] in orders:
                            for j in orders[values[i]]:
                                if j in indices and not visited[indices[j]]:
                                    traverse(indices[j])

                        stack.append(values[i])

                while not all(visited):
                    for i in range(len(visited)):
                        if not visited[i]:
                            traverse(i)

                while stack:
                    sorted.append(stack.pop())

                result += sorted[len(sorted) // 2]

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
