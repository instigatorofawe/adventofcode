import sys
import heapq


def valid_history(direction, history_3, history_2, history_1):
    match (direction, history_1):
        case ("up", "down"):
            return False
        case ("down", "up"):
            return False
        case ("left", "right"):
            return False
        case ("right", "left"):
            return False
    return not (
        direction == history_3 and direction == history_2 and direction == history_1
    )


def valid_history_b(direction, history):
    if history[-1] == "none":
        return True
    match (direction, history[-1]):
        case ("up", "down"):
            return False
        case ("down", "up"):
            return False
        case ("left", "right"):
            return False
        case ("right", "left"):
            return False
    if history[-1] != direction:
        for i in range(2, 5):
            if history[-i] != history[-1]:
                return False
        return True
    else:
        for i in range(9):
            if history[i] != direction:
                return True
        return False


def part_a(lines: list[str]):
    height = len(lines)
    width = len(lines[0])
    costs = [[int(x) for x in line] for line in lines]

    visited: set[tuple[int, int, str, str, str]] = set()

    queue = [(0, 0, 0, "none", "none", "none")]  # Distance, row, column, history
    result = sys.maxsize

    while queue:
        distance, i, j, history_3, history_2, history_1 = heapq.heappop(queue)

        if (i, j, history_3, history_2, history_1) not in visited:
            visited.add((i, j, history_3, history_2, history_1))
            if i == height - 1 and j == width - 1:
                result = min(result, distance)
            else:
                neighbors = (
                    (i + 1, j, "up"),
                    (i - 1, j, "down"),
                    (i, j + 1, "right"),
                    (i, j - 1, "left"),
                )

                for x, y, direction in neighbors:
                    if (
                        0 <= x < height
                        and 0 <= y < width
                        and valid_history(direction, history_3, history_2, history_1)
                        and (x, y, history_2, history_1, direction) not in visited
                    ):
                        heapq.heappush(
                            queue,
                            (
                                distance + costs[x][y],
                                x,
                                y,
                                history_2,
                                history_1,
                                direction,
                            ),
                        )

    print(result)


def part_b(lines: list[str]):
    height = len(lines)
    width = len(lines[0])
    costs = [[int(x) for x in line] for line in lines]

    visited: set[
        tuple[int, int, tuple[str, str, str, str, str, str, str, str, str, str]]
    ] = set()

    queue = [
        (
            0,
            0,
            0,
            (
                "none",
                "none",
                "none",
                "none",
                "none",
                "none",
                "none",
                "none",
                "none",
                "none",
            ),
        )
    ]  # Distance, row, column, history
    result = sys.maxsize

    while queue:
        distance, i, j, history = heapq.heappop(queue)

        if (i, j, history) not in visited:
            visited.add((i, j, history))
            if (
                i == height - 1
                and j == width - 1
                and (history[-1] == history[-2] == history[-3] == history[-4])
            ):
                result = min(result, distance)
            else:
                neighbors = (
                    (i + 1, j, "up"),
                    (i - 1, j, "down"),
                    (i, j + 1, "right"),
                    (i, j - 1, "left"),
                )

                for x, y, direction in neighbors:
                    if (
                        0 <= x < height
                        and 0 <= y < width
                        and valid_history_b(direction, history)
                        and (
                            x,
                            y,
                            (
                                history[-9],
                                history[-8],
                                history[-7],
                                history[-6],
                                history[-5],
                                history[-4],
                                history[-3],
                                history[-2],
                                history[-1],
                                direction,
                            ),
                        )
                        not in visited
                    ):
                        heapq.heappush(
                            queue,
                            (
                                distance + costs[x][y],
                                x,
                                y,
                                (
                                    history[-9],
                                    history[-8],
                                    history[-7],
                                    history[-6],
                                    history[-5],
                                    history[-4],
                                    history[-3],
                                    history[-2],
                                    history[-1],
                                    direction,
                                ),
                            ),
                        )

    print(result)


def run():
    lines = [line.strip() for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
