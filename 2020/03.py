def load_map():
    tobogan_map = []

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            tobogan_map.append(line.strip())

    return tobogan_map


def part1(right, down):
    tobogan_map = load_map()
    trees = 0
    j = right

    for i in range(down, len(tobogan_map), down):
        if tobogan_map[i][j] == "#":
            trees += 1
        j += right
        j = j % len(tobogan_map[i])

    print(trees)
    return trees


def part2():
    total = 1
    for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees = part1(right, down)
        total *= trees
    print(total)
