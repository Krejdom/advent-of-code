def load_file():
    output = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            line = line.replace("(", "( ").replace(")", " )")
            line = line.split()
            output.append(line)
        return output


def solve_par(e):
    left = e.index("(")
    right = left
    left_count = 1
    right_count = 0

    while left_count != right_count:
        right += 1
        if e[right] == "(":
            left_count += 1
        elif e[right] == ")":
            right_count += 1

    return e[:left], e[left+1:right], e[right+1:]


def ev1(e):
    if len(e) == 1:
        return int(e[0])

    if "(" in e:
        l, m, r = solve_par(e)
        return ev1(l + [ev1(m)] + r)

    if e[-2] == "+": 
        return ev1(e[:-2]) + int(e[-1])
    elif e[-2] == "*":
        return ev1(e[:-2]) * int(e[-1])


def ev2(e):
    if len(e) == 1:
        return int(e[0])

    if "(" in e:
        l, m, r = solve_par(e)
        return ev2(l + [ev2(m)] + r)

    if "*" in e:
        times_position = e.index("*")
        return ev2(e[:times_position]) * ev2(e[times_position + 1:])
    elif "+" in e:
        plus_position = e.index("+")
        return ev2(e[:plus_position]) + ev2(e[plus_position + 1:])


def part1():
    total = 0
    for e in load_file():
        total += ev1(e)
    print(total)


def part2():
    total = 0
    for e in load_file():
        total += ev2(e)
    print(total)
