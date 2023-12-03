def load_input():
    doc = []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            doc.append(line)
    return doc


def get_symbols_coords(schematic):
    symbol_coords = set()

    for x, line in enumerate(schematic):
        for y, symbol in enumerate(line):
            if (not(symbol.isnumeric()) and
                symbol != "." and
                symbol != "\n"):
                symbol_coords.add((x, y))
    return symbol_coords


def is_engine_part(x, y, part_len, symbol_coords):
    if ((x, y) in symbol_coords or          # after
        (x, y-part_len-1) in symbol_coords  # before
        ):
        return True
    for i in range(part_len+2):
        if ((x-1, y-part_len-1+i) in symbol_coords or   # above
            (x+1, y-part_len-1+i) in symbol_coords):    # below
            return True
    return False


def part_1():
    part_nums_sum = 0
    engine_schematic = load_input()
    symbol_coords = get_symbols_coords(engine_schematic)

    engine_part = ""
    for x, line in enumerate(engine_schematic):
        for y, symbol in enumerate(line):
            if symbol.isnumeric():
                engine_part += symbol
            elif not symbol.isnumeric() and engine_part != "":
                if is_engine_part(x, y, len(engine_part), symbol_coords):
                    part_nums_sum += int(engine_part)
                engine_part = ""
    print(part_nums_sum)


def get_asterisk_coords(schematic):
    asterisk_coords = set()

    for x, line in enumerate(schematic):
        for y, symbol in enumerate(line):
            if symbol == "*":
                asterisk_coords.add((x, y))
    return asterisk_coords


def get_right(x, y, schematic):
    num = ""
    y += 1
    while schematic[x][y].isnumeric():
        num += schematic[x][y]
        y += 1
    return int(num)


def get_left(x, y, schematic):
    num = ""
    y -= 1
    while schematic[x][y].isnumeric():
        num = schematic[x][y] + num
        y -= 1
    return int(num)


def get_top_bottom(x, y, schematic):
    adj_nums = []
    num = ""
    if schematic[x][y] == ".":
        if schematic[x][y-1].isnumeric():
            adj_nums.append(get_left(x, y, schematic))
        if schematic[x][y+1].isnumeric():
            adj_nums.append(get_right(x, y, schematic))
    else:
        while schematic[x][y].isnumeric():
            y += 1
        adj_nums.append(get_left(x, y, schematic))
    return adj_nums


def part_2():
    gear_ratios_sum = 0
    schematic = load_input()
    asterisk_coords = get_asterisk_coords(schematic)
    for x, y in asterisk_coords:
        adj_nums = []
        if schematic[x][y+1].isnumeric():
            adj_nums.append(get_right(x, y, schematic))
        if y != 0 and schematic[x][y-1].isnumeric():
            adj_nums.append(get_left(x, y, schematic))
        if x != 0 and ((y != 0 and schematic[x-1][y-1].isnumeric()) or
                       schematic[x-1][y].isnumeric() or
                       schematic[x-1][y+1].isnumeric()):
            adj_nums += get_top_bottom(x-1, y, schematic)
        if (x != len(schematic) and
            ((y != 0 and schematic[x+1][y-1].isnumeric()) or
             schematic[x+1][y].isnumeric() or
             schematic[x+1][y+1].isnumeric())):
            adj_nums += get_top_bottom(x+1, y, schematic)
        
        if len(adj_nums) == 2:
            gear_ratios_sum += adj_nums[0] * adj_nums[1]
    
    print(gear_ratios_sum)

            
if __name__ == '__main__':
    part_1()
    part_2()
