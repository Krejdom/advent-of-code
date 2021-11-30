def load_file():
    with open("input.txt", "r") as f:
        return [int(i) for i in f.readline().split(",")]


def part1():
    numbers = load_file()

    i = len(numbers)
    while i < 2020:
        last_number = numbers[i-1]

        n = i - 2
        while n >= 0:
            if numbers[n] == last_number:
                numbers.append(i - n - 1)
                break
            n -= 1

        if n == -1:
            numbers.append(0)

        i += 1

    print(numbers[-1])


def part2():
    numbers = load_file()
    last_map = {}

    for n in range(len(numbers)-1):
        last_map[numbers[n]] = n

    i = len(numbers)
    while i < 30000000:
        n = numbers[i-1]

        if n in last_map:
            numbers.append(i - last_map[n] - 1)
        else:
            numbers.append(0)

        last_map[n] = i - 1
        i += 1

    print(numbers[-1])
