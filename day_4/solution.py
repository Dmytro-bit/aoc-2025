from day_4.input import DATA


def check_neighbors(matrix, y, x, bound):
    total = 0
    positions = [  # (y, x)
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

    for (temp_y, temp_x) in positions:
        new_y = temp_y + y
        new_x = temp_x + x

        if (new_y >= len(matrix)) or (new_y < 0) or (new_x >= len(matrix[y]) or (new_x < 0)):
            continue

        if matrix[new_y][new_x] == "@":
            total += 1

    if total < bound:
        return True

    return False


def part1(string: str):
    matrix = string.split("\n")
    total_rolls = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] != "@":
                continue

            if check_neighbors(matrix, y, x, 4):
                total_rolls += 1

    return total_rolls


def part2(string: str):
    matrix = string.split("\n")
    total_rolls = 0
    new = True

    while new:
        new = False
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] != "@":
                    continue

                if check_neighbors(matrix, y, x, 4):
                    new = True
                    total_rolls += 1

                    matrix[y] = matrix[y][:x] + "." + matrix[y][x + 1:]

    return total_rolls


if __name__ == "__main__":
    print(part1(DATA))
    print(part2(DATA))
