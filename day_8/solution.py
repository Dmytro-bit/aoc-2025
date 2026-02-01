from functools import reduce
from itertools import combinations
from operator import mul

from day_8.input import TEST_DATA, DATA

Coord = tuple[int, int, int]


class QuickUnionDisjointSet:

    def __init__(self, size: int):
        self._ids = list(range(size))
        self.count = size
        self.sizes = [1] * size

    def find(self, p):
        while self._ids[p] != p:
            p = self._ids[p]

        return p

    def union(self, p, q):

        self._rootP = self.find(p)
        self._rootQ = self.find(q)

        if (self._rootP == self._rootQ):
            return None

        self._ids[self._rootP] = self._rootQ

        self.sizes[self._rootQ] += self.sizes[self._rootP]
        self.sizes[self._rootP] = 1

        self.count -= 1
        return None


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

    ds = QuickUnionDisjointSet(len(junctions))

    for i in range(limit):
        ds.union(pairs[i][0][0], pairs[i][1][0])

    return reduce(mul, sorted(ds.sizes, reverse=True)[:3], 1)


def part2(string: str):
    junctions = parse(string)

    pairs = list(combinations(junctions, 2))

    pairs.sort(key=lambda pair: distance_sqr(pair[0][1], pair[1][1]))

    ds = QuickUnionDisjointSet(len(junctions))

    for i in range(len(pairs)):
        p1 = pairs[i][0]
        p2 = pairs[i][1]


        ds.union(p1[0], p2[0])

        if ds.count == 1:
            return p1[1][0] * p2[1][0]

    return None


if __name__ == "__main__":
    print("p1.test", part1(TEST_DATA, 10))
    print("p1.main", part1( DATA, 1000))

    print("p2.test", part2(TEST_DATA))
    print("p2.data", part2(DATA))

