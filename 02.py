def parse_policy(row):
    policy_parts = row.split(" ")
    first, second = map(int, policy_parts[0].split("-"))

    return first, second, policy_parts[1][0], policy_parts[2]


def part_1():
    counter = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        for row in f:
            first, second, letter, password = parse_policy(row)
            occurance = password.count(letter)

            if occurance >= first and occurance <= second:
                counter += 1

    print(counter)


def part_2():
    counter = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        for row in f:
            first, second, letter, password = parse_policy(row)

            if (password[first-1] == letter) != (password[second-1] == letter):
                counter += 1

    print(counter)


if __name__ == '__main__':
    part_1()
    part_2()
