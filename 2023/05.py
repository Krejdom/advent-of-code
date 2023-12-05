def load_input():
    seeds = []
    mappings = []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line[0:6] == "seeds:":
                seeds = [int(i) for i in line[7:].split()]
            else:
                mappings.append(line)
    return seeds, mappings[1:]


def parse_maps(mappings):
    parsed_maps = []
    m = []
    for line in mappings:
        if line == "\n":
            parsed_maps.append(m)
            m = []
        elif line[0].isnumeric():
            m.append([int(i) for i in line.split()])
    parsed_maps.append(m)
    return parsed_maps


def get_lowest_location(seeds, mappings):
    min_location = float("inf")
    for seed in seeds:
        s = seed
        for mapping in mappings:
            for m in mapping:
                if s >= m[1] and s <= m[1]+m[2]-1:
                    s = m[0] + (s - m[1])
                    break   # don't convert twice
        if s < min_location:
            min_location = s
    
    return min_location


def part_1():
    seeds, mappings = load_input()
    mappings = parse_maps(mappings)
    print(get_lowest_location(seeds, mappings)) 


def part_2():
    pass


if __name__ == '__main__':
    part_1()
    part_2()
