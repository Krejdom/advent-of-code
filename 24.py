def load_file(file_path):
    tiles = []
    with open(file_path, "r") as f:
        for line in f:
            x, y = 0, 0
            line = line.strip()
            while line:
                if line[0] == "e":
                    x += 1
                    y -= 1
                    line = line[1:]
                
                elif line[0] == "w":
                    x -= 1
                    y += 1
                    line = line[1:]

                elif line[:2] == "nw":
                    y += 2
                    line = line[2:]

                elif line[:2] == "se":
                    y -= 2
                    line = line[2:]

                elif line[:2] == "ne":
                    x += 1
                    y += 1
                    line = line[2:]

                elif line[:2] == "sw":
                    x -= 1
                    y -= 1
                    line = line[2:]

                else:
                    print("Unknown")

            tiles.append((x, y))
    return tiles


def neighbours_colors(tile, tiles):
    black = 0
    white = 0
    x, y = tile

    for coords in [(x, y-2), (x, y+2), (x+1, y-1),
                   (x-1, y+1), (x+1, y+1), (x-1, y-1)]:
        if coords in tiles:
            if tiles[coords] == 0:
                black += 1
            elif tiles[coords] == 1:
                white += 1
            else:
                print("Unknown")

    return black, white


def add_neighbours(tiles):
    new_tiles = {}
    for tile in tiles:
        x, y = tile
        for coords in [(x, y-2), (x, y+2), (x+1, y-1),
                       (x-1, y+1), (x+1, y+1), (x-1, y-1)]:
            if coords not in tiles:
                new_tiles[coords] = 1
        new_tiles[tile] = tiles[tile]

    return new_tiles


def flip(tiles_color):
    new_tiles_color = {}

    for tile, color in tiles_color.items():
        black_n, white_n = neighbours_colors(tile, tiles_color)
        if color == 0:
            if black_n == 0 or black_n > 2:
                new_tiles_color[tile] = 1
            else:
                new_tiles_color[tile] = 0
        elif color == 1:
            if black_n == 2:
                new_tiles_color[tile] = 0
            else:
                new_tiles_color[tile] = 1
    return new_tiles_color


def part1():
    tiles = load_file("input.txt")
    unique_tiles = set(tiles)

    black = 0
    for tile in unique_tiles:
        if tiles.count(tile) % 2 == 1:
            black += 1

    print(black)


def part2():
    tiles = load_file("input.txt")
    unique_tiles = set(tiles)

    tiles_color = {}

    for tile in unique_tiles:
        if tiles.count(tile) % 2 == 1:
            tiles_color[tile] = 0
        else:
            tiles_color[tile] = 1

    for i in range(100):
        tiles_color = add_neighbours(tiles_color)
        tiles_color = flip(tiles_color)

        black = 0
        for t in tiles_color:
            if tiles_color[t] == 0:
                black += 1

        print("Day", str(i+1) + ":", black)


part1()
part2()
