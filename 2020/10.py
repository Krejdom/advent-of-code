def load_file(file_path="input.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return sorted([int(i) for i in f.readlines()] + [0])


def part1():
    joilts = load_file();
    one = 0
    three = 1

    for i in range(len(joilts) - 1):
        if joilts[i+1] - joilts[i] == 1:
            one += 1
        elif joilts[i+1] - joilts[i] == 3:
            three += 1
        else:
            print("cannot connect")

    print(one * three)


def part2():
    joilts = load_file()
    comb = {} 
    for i in range(len(joilts) - 3):
        comb[i] = []
        for j in range(i + 1, i + 4):
            if joilts[j] - joilts[i] <= 3:
                comb[i].append(j)
            else:
                break

    for i in range(len(joilts) - 3, len(joilts) - 1):
        comb[i] = []
        for j in range(i + 1, len(joilts)):
            if joilts[j] - joilts[i] <= 3:
                comb[i].append(j)
            else:
                break
    return comb


def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper


# https://www.python-course.eu/python3_memoization.php
@memoize
def count_connections(joilt_index):
    if joilt_index == len(comb):
        return 1

    elif len(comb[joilt_index]) == 1:
        return count_connections(comb[joilt_index][0])
    elif len(comb[joilt_index]) == 2:
        return (count_connections(comb[joilt_index][0]) +
                count_connections(comb[joilt_index][1]))
    elif len(comb[joilt_index]) == 3:
        return (count_connections(comb[joilt_index][0]) +
                count_connections(comb[joilt_index][1]) +
                count_connections(comb[joilt_index][2]))
    else:
        print(comb[joilt_index])
        print("else")    

part1()
comb = part2()
print(count_connections(0))
