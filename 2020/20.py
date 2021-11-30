import numpy as np


SEA_MONSTER = [(0, 18),
               (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
               (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
SM_WIDTH = 20
SM_HEIGHT = 3


class Tile():
    def __init__(self, tile_id, tile_content):
        self.content = tile_content
        self.tile_id = tile_id

        self.image = self.get_image(tile_content)
        self.edges = self.get_edges(tile_content)   # top, left, bottom, right

        self.rotation = 0
        self.flipped = False

        self.neighbours = [None, None, None, None]
        self.in_place = False


    def __str__(self):
        return self.tile_id


    def get_edges(self, tile_content):
        edges = [[], [], [], []]
        edges[0] = list(tile_content[0])
        edges[2] = list(tile_content[-1][::-1])

        for line in tile_content:
            edges[3].append(line[0])
            edges[1].append(line[-1])
        edges[3] = edges[3][::-1]

        return edges


    def get_image(self, tile_content):
        without_borders = []
        for line in tile_content[1:-1]:
            without_borders.append(line[1:-1])
        return without_borders


    def is_corner(self):
        """Can be called only after all pieces were loaded and function
        mark_borders was called."""
        return self.edges.count("border") == 2


    def rotate(self, n):
        for _ in range(n):
            # clockwise
            # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
            self.image = list(zip(*self.image[::-1]))
            self.content = list(zip(*self.content[::-1]))
            self.edges = [self.edges[-1]] + self.edges[:-1]
            self.neighbours = [self.neighbours[-1]] + self.neighbours[:-1]
            self.rotation = (self.rotation + 1) % 4


    def flip(self):
        self.content = flip(self.content)
        self.image = self.get_image(self.content)
        self.edges = self.get_edges(self.content)
        self.neighbours[0], self.neighbours[3] = self.neighbours[3], self.neighbours[0]
        self.neighbours[1], self.neighbours[2] = self.neighbours[2], self.neighbours[1],
        self.flipped = True


def load_tiles(input_file):
    tiles = []
    with open(input_file, "r", encoding="utf-8") as f:

        for line in f:
            if line[:4] == "Tile":
                tile_content = []
                tile_id = line[5:-2]

            elif line == "\n":
                tile = Tile(tile_id, tile_content)
                tiles.append(tile)

            elif line[0] == "." or line[0] == "#":
                tile_content.append(list(line.strip()))

            else:
                print("unknown")

        tile = Tile(tile_id, tile_content)
        tiles.append(tile)    # append the last tile

    return tiles


def draw_puzzle(puzzle):
    for row in puzzle:
        for symbol in row:
            print(symbol, end="")
        print()


def is_border(edge, tile, tiles):
    for tile2 in tiles:
        if tile == tile2:
            continue

        for edge2 in tile2.edges:
            if edge == edge2 or edge == edge2[::-1]:
                return False

    return True


def mark_borders(tile, tiles):
    """Set edges and neighbours as border."""
    for i, edge in enumerate(tile.edges):
        if is_border(edge, tile, tiles):
            tile.edges[i] = "border"
            tile.neighbours[i] = "border"


def add_neighbour(tile, i, tile2, j):
    tile2.neighbours[j] = tile
    tile.neighbours[i] = tile2
    tile2.in_place = True


def flip(matrix):
    new_matrix = [["" for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix


def find_neighbours(tile, tiles):
    for i, edge in enumerate(tile.edges):
        # Skip if there is already a tile or it is a border
        if (edge == "border") or (tile.neighbours[i] is not None):
            continue

        for tile2 in tiles:
            if tile == tile2:
                continue

            j = (i + 2) % 4     # neighbouring side
            
            if tile2.in_place:
                if edge == tile2.edges[j][::-1]:
                    add_neighbour(tile, i, tile2, j)
                continue

            # Try to rotate the piece and add it to the puzzle
            for _ in range(4):
                if edge == tile2.edges[j][::-1]:
                    add_neighbour(tile, i, tile2, j)
                    break
                tile2.rotate(1)

            # If the previous did not work, flip the tile2 and try again
            if tile.neighbours[i] is None:
                tile2.flip()
                for _ in range(4):
                    if edge == tile2.edges[j][::-1]:
                        add_neighbour(tile, i, tile2, j)
                        break
                    tile2.rotate(1)

    # Recursively find other neighbours
    for neighbour in tile.neighbours:
        if neighbour is not None and neighbour != "border":
            if None in neighbour.neighbours:
                find_neighbours(neighbour, tiles)


def get_first_corner(tiles):
    for tile in tiles:
        if tile.is_corner():
            tl_tile = tile
            break

    # Rotate the corner, so it is a top left one
    while not (tl_tile.edges[0] == "border" and
               tl_tile.edges[3] == "border"):
        tl_tile.rotate(1)

    tl_tile.in_place = True
    return tl_tile


def print_neighbour_status(tiles):
    for tile in tiles:
        print(tile.tile_id, end=" ::: ")
        for t in tile.neighbours:
            if t == "border":
                print("----", end=" ")
            else:
                print(t.tile_id, end=" ")
        print()


def join_puzzle(tl_tile):
    puzzle = []
    y_tile = tl_tile
    while y_tile != "border":
        x_tile = y_tile
        puzzle_line = x_tile.image
        x_tile = x_tile.neighbours[1]
        while x_tile != "border":
            puzzle_line = np.concatenate((puzzle_line, x_tile.image), axis=1)
            x_tile = x_tile.neighbours[1]
        if len(puzzle) == 0:
            puzzle = puzzle_line
        else:
            puzzle = np.concatenate((puzzle, puzzle_line), axis=0)
        y_tile = y_tile.neighbours[2]

    return puzzle


def find_see_monster(puzzle):
    new_puzzle = [list(puzzle_line) for puzzle_line in puzzle]
    for col in range(len(puzzle) - SM_HEIGHT):
        for row in range(len(puzzle[0]) - SM_WIDTH):
            is_sea_monser = True
            for y, x in SEA_MONSTER:
                if puzzle[col + y][row + x] != "#" and puzzle[col + y][row + x] != "O":
                    is_sea_monser = False
                    break

            if is_sea_monser:
                for y, x in SEA_MONSTER:
                    new_puzzle[col + y][row + x] = "O"

    return new_puzzle


def part1():
    tiles = load_tiles("input.txt")
    
    result = 1
    # Find all borders
    for tile in tiles:
        mark_borders(tile, tiles)
        if tile.is_corner():
            result *= int(tile.tile_id)

    return result


def part2():
    tiles = load_tiles("input.txt")

    # Find all borders
    for tile in tiles:
        mark_borders(tile, tiles)

    # Get top left corner
    tl_tile = get_first_corner(tiles)

    # Find neighbours of the top left corner
    find_neighbours(tl_tile, tiles)

    # Join puzzle
    puzzle = join_puzzle(tl_tile)

    # Find see monsters in all (also flippd) rotations 
    for _ in range(2):
        for _ in range(4):
            puzzle = find_see_monster(puzzle)
            puzzle = list(zip(*puzzle[::-1]))   # rotation

        puzzle = flip(puzzle)


    return sum([puzzle_line.count("#") for puzzle_line in puzzle])
