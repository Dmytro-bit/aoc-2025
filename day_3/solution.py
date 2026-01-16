from day_3.input import DATA


def part1(string: str):
    total_joltage = 0

    for pack in string.split("\n"):
        temp: str = "0"
        p1, p2 = 0, 1

        while p2 < len(pack):

            if (int(pack[p2]) > int(pack[p1])) and (p2 < len(pack) - 1):
                p1 = p2
                p2 += 1
                temp = pack[p2]

            elif int(pack[p2]) > int(temp):
                temp = pack[p2]

            else:
                p2 += 1

        total_joltage += int(pack[p1] + temp)

    return total_joltage


def part2(string: str):
    required_len = 12

    total_joltage = 0

    for pack in string.split("\n"):
        stack = []
        changes = len(pack) - required_len
        for jolt in pack:
            while (len(stack) > 0) and (stack[-1] < jolt) and (changes >= 1):
                stack.pop()
                changes -= 1

            if len(stack) < required_len:
                stack.append(jolt)
            else:
                changes -= 1

        total_joltage += int("".join(stack))

    return total_joltage


if __name__ == "__main__":
    print(part1(DATA))
    print(part2(DATA))
