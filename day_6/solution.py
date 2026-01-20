import re
from functools import reduce
from operator import mul

from day_6.input import DATA, TEST_DATA


def matrix_convertor(rows):
    num_matrix = []
    length = len(rows)

    pattern = r'(\d+)'
    op_pattern = r'[\*\+]'

    for row in rows[:(length - 1)]:
        num_row = re.findall(pattern, row)
        num_matrix.append(tuple(num_row))

    operations_matrix = re.findall(op_pattern, rows[-1])
    return num_matrix, operations_matrix


def part1(string: str):
    result = 0
    rows = string.split("\n")

    matrix, operations = matrix_convertor(rows)

    for i in range(len(matrix[0])):
        nums = [int(num[i]) for num in matrix]
        if operations[i] == "*":
            result += reduce(mul, nums)
        else:
            result += sum(nums)

    return result


def matrix_convertor2(rows):
    pattern = r'([*+]\s+)(?= [*+]|$)'
    op_pattern = r'[\*\+]'
    matrix = []

    ranges = [(m.start(), m.end()) for m in re.finditer(pattern, rows[-1])]

    for row in rows[:len(rows) - 1]:
        tem_row = []

        for (start, end) in ranges:
            tem_row.append(row[start: end])

        matrix.append(tem_row)

    operations_matrix = re.findall(op_pattern, rows[-1])

    return matrix, operations_matrix


def part2(string: str):
    result = 0
    rows = string.split("\n")
    matrix, operations = matrix_convertor2(rows)

    for column in range(len(matrix[0])):
        nums = [num[column] for num in matrix]
        new_nums = []
        for i in range(len(max(nums))):
            tmp = ""
            for num in nums:

                if num[i] != " ":
                    tmp += num[i]

            print(tmp, column, i)
            new_nums.append(int(tmp))

        if operations[column] == "*":
            result += reduce(mul, new_nums)
        else:
            result += sum(new_nums)

    return result


if __name__ == "__main__":
    print(part1(DATA))
    print(part2(DATA))
