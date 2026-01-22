from functools import lru_cache

from day_7.input import DATA


def part1(string: str):
    count = 0
    matrix = string.split('\n')
    prev_row = [("|" if i == 'S' else "") for i in matrix[0]]

    for y in range(1, len(matrix)):
        curr_row = prev_row
        for x in range(len(matrix[0])):

            if (matrix[y][x] == "^") and (prev_row[x] == "|"):
                curr_row[x - 1] = "|"
                curr_row[x + 1] = "|"
                curr_row[x] = ""
                count += 1

        prev_row = curr_row

    return count


@lru_cache(None)
def start_time_line(matrix, y, point_x):
    if y >= len(matrix):
        return 0

    count = 0

    if matrix[y][point_x] == "^":
        count += 1
        count += start_time_line(matrix, y + 1, point_x - 1)
        count += start_time_line(matrix, y + 1, point_x + 1)

    else:
        count += start_time_line(matrix, y + 1, point_x)

    return count


def part2(string: str):
    matrix = tuple(string.split('\n'))
    point_x = matrix[0].index("S")
    count = start_time_line(matrix, 1, point_x)
    return count + 1


if __name__ == "__main__":
    print(part1(DATA))
    print(part2(DATA))
