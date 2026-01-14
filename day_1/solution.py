from input import DATA


def part1(string: str) -> int:
    total_count = 0
    current = 50
    for i in string.split("\n"):
        direction, num = i[:1], int(i[1:])

        if direction == 'L':
            current = (current - num) % 100

        else:
            current = (current + num) % 100

        if current == 0:
            total_count += 1

    return total_count


def part2(string: str):
    total_count = 0
    current = 50
    for i in string.split("\n"):
        direction, num = i[:1], int(i[1:])

        if direction == 'L':
            temp = current - num

            total_count += abs((current - 1) // 100 - (temp - 1) // 100)

            current = temp % 100

        else:
            current = current + num

            total_count += current // 100

            current = current % 100

    return total_count


if __name__ == "__main__":
    print(part1(DATA))
    print(part2(DATA))
