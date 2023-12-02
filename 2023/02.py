def load_input():
    doc = []

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            game = line.strip().split(": ")[1].split("; ")
            game_dict = {
                "red"   : 0,
                "green" : 0,
                "blue"  : 0
            }
            for reveal in game:
                reveal = reveal.split(", ")
                for color_pair in reveal:
                    number = int(color_pair.split(" ")[0])
                    color = color_pair.split(" ")[1]
                    if color == "red":
                        if number > game_dict["red"]:
                            game_dict["red"] = number
                    elif color == "green":
                        if number > game_dict["green"]:
                            game_dict["green"] = number
                    elif color == "blue":
                        if number > game_dict["blue"]:
                            game_dict["blue"] = number
                    else:
                        pass
            doc.append(game_dict)
    return doc


def part_1():
    ids_sum = 0
    games_record = load_input()
    game_n = 1
    for game in games_record:
        if (game["red"] <= 12 and
            game["green"] <= 13 and
            game["blue"] <= 14):
            ids_sum += game_n
        game_n += 1

    print(ids_sum)

def part_2():
    power_sum = 0
    games_record = load_input()

    for game in games_record:
        power_sum += game["red"] * game["green"] * game["blue"]

    print(power_sum)


if __name__ == '__main__':
    part_1()
    part_2()
