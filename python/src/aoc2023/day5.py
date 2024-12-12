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

    def map_ranges(self, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        result: list[tuple[int, int]] = []

        segment_index = 0
        while ranges:
            start, end = ranges.pop()
            while (
                segment_index < len(self.segments)
                and self.segments[segment_index][1] < start
            ):
                segment_index += 1

            if (
                segment_index == len(self.segments)
                or end < self.segments[segment_index][0]
                or start > self.segments[segment_index][1]
            ):
                result.append((start, end))
            else:
                if start < self.segments[segment_index][0]:
                    result.append(
                        (start, min(end, self.segments[segment_index][0] - 1))
                    )

                result.append(
                    (
                        max(start, self.segments[segment_index][0])
                        + self.segments[segment_index][2],
                        min(end, self.segments[segment_index][1])
                        + self.segments[segment_index][2],
                    )
                )
                if end > self.segments[segment_index][1]:
                    ranges.append((self.segments[segment_index][1] + 1, end))
        result.sort()

        current_start = result[0][0]
        current_end = result[0][1]

        merged_result: list[tuple[int, int]] = []

        for i in range(1, len(result)):
            if result[i][0] <= current_end + 1:
                current_end = result[i][1]
            else:
                merged_result.append((current_start, current_end))
                current_start, current_end = result[i]
        merged_result.append((current_start, current_end))

        return merged_result

    @override
    def __repr__(self) -> str:
        return str(self.segments)


def part_a(lines: list[str]):

    maps = [Map() for _ in range(7)]
    map_index: int = -1

    lines = iter(lines)
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
    pass


def part_b(lines: list[str]):
    maps = [Map() for _ in range(7)]
    map_index: int = -1

    lines = iter(lines)
    seeds = [int(x) for x in next(lines).split(":")[1].split()]
    seed_ranges = [
        (seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1] - 1)
        for i in range(len(seeds) // 2)
    ]
    seed_ranges.sort()

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

    for i in range(7):
        seed_ranges.reverse()
        seed_ranges = maps[i].map_ranges(seed_ranges)

    print(seed_ranges[0][0])


def run():
    lines = [line for line in sys.stdin]
    part_a(lines)
    part_b(lines)


if __name__ == "__main__":
    run()
