import copy


def load_file(file_path="input.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        seats = []
        for line in f.readlines():
            row = []
            for space in line.strip():
                row.append(space)
            seats.append(row)
    return seats


def adj_occupied(row, col, seats):
    occupied = 0

    width = len(seats[0])
    height = len(seats)
    
    for r, c in [(0, 1), (1, 0), (1, 1), (-1, 0),
                 (0, -1), (-1, -1), (1, -1), (-1, 1)]:
        r += row
        c += col
        if r >= 0 and r < height and c >= 0 and c < width:
            if seats[r][c] == "#":
                occupied += 1

    return occupied


def visible_occupied(row, col, seats):
    occupied = 0

    width = len(seats[0])
    height = len(seats)
    
                #   R       D       U        L
    for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0),
                #  DR        UL       DL       UR
                 (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        x = row + r
        y = col + c

        while x >= 0 and x < height and y >= 0 and y < width:
            if seats[x][y] == "#":
                occupied += 1
                break
            elif seats[x][y] == "L":
                break
            x += r
            y += c

    return occupied


def apply_rules(seats, tolerance, other_occupied):
    new_seats = copy.deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] == ".":
                continue
            elif (seats[row][col] == "L" and
                  other_occupied(row, col, seats) == 0):
                new_seats[row][col] = "#"
            elif (seats[row][col] == "#" and
                  other_occupied(row, col, seats) >= tolerance):
                new_seats[row][col] = "L"
    return new_seats


def are_same(board1, board2):
    for x in range(len(board1)):
        for y in range(len(board2)):
            if board1[x][y] != board2[x][y]:
                return False
    return True


def simulate(tolerance, other_occupied):
    board = load_file()
    nxt_board = apply_rules(load_file(), tolerance, other_occupied)

    while not are_same(board, nxt_board):
        board = nxt_board
        nxt_board = apply_rules(board, tolerance, other_occupied)

    occupied = 0
    for row in board:
        for place in row:
            if place == "#":
                occupied += 1

    print(occupied)


def part1():
    simulate(4, adj_occupied)


def part2():
    simulate(5, visible_occupied)
