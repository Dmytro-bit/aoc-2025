from functools import reduce
from itertools import combinations
from operator import mul
from typing import Self

from day_8.input import TEST_DATA, DATA

CIRCUIT_MAP = {}


class Circuit:
    def __init__(self, *args):
        self.junctions = set(args)

        for i in self.junctions:
            CIRCUIT_MAP[i] = self

    def __contains__(self, item):
        return item in self.junctions

    def __len__(self):
        return len(self.junctions)

    def __repr__(self):
        return f"{len(self.junctions)}:  {self.junctions.__str__()}"

    def __or__(self, other: Self):
        return Circuit(*self.junctions, *other.junctions)

    def add(self, point):
        self.junctions.add(point)


Coord = tuple[int, int, int]


def parse(string: str) -> list[Coord]:
    return [(index, tuple(map(int, line.split(",")))) for index, line in enumerate(string.split("\n"))]


def distance_sqr(p1: Coord, p2: Coord):
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2


def part1(string: str, limit):
    junctions = parse(string)

    pairs = list(combinations(junctions, 2))

    pairs.sort(key=lambda pair: distance_sqr(pair[0][1], pair[1][1]))

    circuits = [Circuit(i) for i in junctions]

    for i in range(1, limit):

        p1 = pairs[i][0]
        p2 = pairs[i][1]

        if CIRCUIT_MAP[p1] != CIRCUIT_MAP[p2]:
            circuits.remove(CIRCUIT_MAP[p1])
            circuits.remove(CIRCUIT_MAP[p2])

            circuits.append(CIRCUIT_MAP[p1] | (CIRCUIT_MAP[p2]))

    return reduce(mul, sorted(map(len, circuits), reverse=True)[:3], 1)


def part2(string: str):
    junctions = parse(string)

    pairs = list(combinations(junctions, 2))

    pairs.sort(key=lambda pair: distance_sqr(pair[0][1], pair[1][1]))

    circuits = [Circuit(i) for i in junctions]

    for (p1, p2) in pairs:
        if CIRCUIT_MAP[p1] != CIRCUIT_MAP[p2]:
            circuits.remove(CIRCUIT_MAP[p1])
            circuits.remove(CIRCUIT_MAP[p2])

            circuits.append(CIRCUIT_MAP[p1] | (CIRCUIT_MAP[p2]))

        if len(circuits) == 1:
            return p1[1][0] * p2[1][0]

    return None


if __name__ == "__main__":
    print(part2(TEST_DATA))
    print(part2(DATA))
