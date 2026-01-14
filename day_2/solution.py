import re

from day_2.input import DATA


def validID(number: int):
    str_num = str(number)

    if len(str_num) % 2 != 0:
        return True

    middle = int(len(str_num) / 2)
    first_part, second_part = str_num[:middle], str_num[middle:]

    if first_part == second_part:
        return False

    return True


def part1(string: str):
    total_sum = 0
    ranges = string.split(",")

    for curr_range in ranges:
        l_bound, h_bound = map(int, curr_range.split("-"))

        for num in range(l_bound, h_bound + 1):
            if not validID(num):
                total_sum += num

    return total_sum


def part2(string: str):
    total_sum = 0
    ranges = string.split(",")
    pattern = r"^(\d+)\1+$"

    for curr_range in ranges:
        l_bound, h_bound = map(int, curr_range.split("-"))

        for num in range(l_bound, h_bound + 1):
            if re.findall(pattern, str(num)):
                total_sum += num

    return total_sum


if __name__ == "__main__":
    print(part1(DATA))
    print(part2(DATA))
