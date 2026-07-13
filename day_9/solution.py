from day_9.input import DATA, TEST_DATA


def print_2d_matrix(matrix):
    for y in matrix:
        print(y)


def part1(string: str):
    tiles = [tuple(map(int, tile.split(","))) for tile in string.split("\n")]

    max_area = 0

    for index in range(len(tiles) - 1):
        for next_index in range(index + 1, len(tiles)):
            max_area = max(max_area, (abs(tiles[index][1] - tiles[next_index][1]) + 1) * abs(
                (tiles[index][0] - tiles[next_index][0]) + 1))

    return max_area


def drow_line(matrix, start: tuple[int, int], end: tuple[int, int]):
    curr_x = start[0]
    curr_y = start[1]

    if curr_x != end[0]:
        diff = end[0] - curr_x

        if diff > 0:
            for i in range(1, diff):
                matrix[curr_y][start[0] + i] = "#"
        else:
            for i in range(diff + 1, 0):
                matrix[curr_y][start[0] + i] = "#"

    else:
        diff = end[1] - curr_y

        if diff > 0:
            for i in range(1, diff):
                matrix[i][curr_x] = "#"

        else:
            for i in range(diff + 1, 0):
                matrix[i][curr_x] = "#"

def fill_matrix(matrix):
    for y in range(len(matrix)):
        fill = False
        for x, value in enumerate(matrix[y]):
            if (value not in {"#", "X"}) and (fill is False):
                continue

            if value == ".":
                matrix[y][x] = "#"
            else:
                fill = not fill

def compress_matrix(tiles):
    y_map = {}
    x_map = {}

    y_asix = list(set([point[1] for point in tiles]))
    x_asix = list(set([point[0] for point in tiles]))

    y_asix.sort()
    x_asix.sort()

    for i, y in enumerate(y_asix):
        y_map[y] = i

    for i, x in enumerate(x_asix):
        x_map[x] = i

    matrix = [["."] * len(x_asix) for i in range(len(y_asix))]

    prev: tuple[int, int] | None = None

    for (x, y) in tiles:
        matrix[y_map[y]][x_map[x]] = "X"
        if prev:
            drow_line(matrix, prev, (x_map[x], y_map[y]))

        prev = (x_map[x], y_map[y])
    return matrix


def part2(string: str):
    tiles = [tuple(map(int, tile.split(","))) for tile in string.split("\n")]

    matrix = compress_matrix(tiles)
    fill_matrix(matrix)
    print_2d_matrix(matrix)


if __name__ == "__main__":
    print(part1(TEST_DATA))
    # print(part2(TEST_DATA))
