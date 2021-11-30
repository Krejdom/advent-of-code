import itertools


P_LENGTH = 25


def load_file(file_path="input.txt"):
    nums = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            nums.append(int(line.strip()))
    return nums


def part1():
    nums = load_file()
    for i in range(P_LENGTH, len(nums)):
        possible_pairs = list(itertools.combinations(nums[i - P_LENGTH: i], 2))
        is_sum = False

        for pair in possible_pairs:
            if nums[i] == pair[0] + pair[1]:
                is_sum = True
                break

        if not is_sum:
            print(nums[i])
            return nums[i], nums


def part2():
    n, nums = part1()
    for start in range(len(nums)):
        i = start
        summary = 0

        while summary < n:
            summary += nums[i]
            i += 1

        if summary == n and start != i - 1:
            print(max(nums[start:i]) + min(nums[start:i]))
