from math import floor


def get_seat_coordinate(navigation, high):
    low = 0
    for direction in navigation:
        mid = floor((high + low) / 2)
        if direction == "F" or direction =="L":
            high = mid
        else:
            low = mid
    return low


def get_seat_ids():
    seat_ids = []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            row = get_seat_coordinate(line[:7], 128)
            col = get_seat_coordinate(line[7:], 8)
            seat_ids.append((row * 8) + col)
    return seat_ids


def part1():
    print(max(get_seat_ids()))


def part2():
    seat_ids = get_seat_ids()
    seat_ids.sort()

    for i in range(len(seat_ids) - 1):
        if seat_ids[i] == seat_ids[i+1] - 2:
            print(seat_ids[i] + 1)
