import sys
import bisect
from typing import override


class Map:
    def __init__(self):
        # Segments are strictly non-overlapping; (start, end, offset)
        self.segments: list[tuple[int, int, int]] = []

    def add(self, segment: tuple[int, int, int]):
        index = bisect.bisect_right(self.segments, segment)
        self.segments.insert(index, segment)

    def map(self, value: int) -> int:
        index = bisect.bisect_right(self.segments, value, key=lambda x: x[0]) - 1
        if index >= 0 and self.segments[index][1] >= value:
            return value + self.segments[index][2]
        else:
            return value

    @override
    def __repr__(self) -> str:
        return str(self.segments)


def run():
    maps = [Map() for _ in range(7)]
    map_index: int = -1

    lines = iter(sys.stdin)
    seeds = [int(x) for x in next(lines).split(":")[1].split()]

    while True:
        line = next(lines, None)
        if line is None:
            break

        if line == "\n":
            map_index += 1
            _ = next(lines)
        else:
            current_mapping = [int(x) for x in line.split()]
            maps[map_index].add(
                (
                    current_mapping[1],
                    current_mapping[1] + current_mapping[2] - 1,
                    current_mapping[0] - current_mapping[1],
                )
            )

    results: list[int] = []
    for seed in seeds:
        for i in range(7):
            seed = maps[i].map(seed)
        results.append(seed)

    print(min(results))


if __name__ == "__main__":
    run()
