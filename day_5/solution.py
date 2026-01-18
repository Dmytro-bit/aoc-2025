from day_5.input import DATA


def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    start = ranges[0][0]
    end = ranges[0][1]

    for index, ran in enumerate(ranges):
        if end >= ran[0]:
            end = max(ran[1], end)

        else:
            merged.append((start, end))
            start = ran[0]
            end = ran[1]

        if index >= len(ranges) - 1:
            merged.append((start, end))

    return merged


def part1(string: str):
    total = 0
    ranges, ids = string.split("\n\n")

    ranges = ranges.split("\n")
    ids = ids.split("\n")

    ranges = [tuple(map(int, ran.split("-"))) for ran in ranges]
    ranges = merge_ranges(ranges)
    print(ranges)

    for curr_id in ids:
        for ran in ranges:
            if (int(curr_id) >= ran[0]) and (int(curr_id) <= ran[1]):
                total += 1
                break

    return total


def part2(string: str):
    fresh_ingredients = 0

    ranges, _ = string.split("\n\n")
    ranges = ranges.split("\n")
    ranges = [tuple(map(int, ran.split("-"))) for ran in ranges]
    ranges = merge_ranges(ranges)

    for ran in ranges:
        fresh_ingredients += ran[1] - ran[0] + 1

    return fresh_ingredients


if __name__ == "__main__":
    print(part1(DATA))
    print(part2(DATA))
