def load_file(file_path="input.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def parse_commands(commands):
    parsed_commands = []
    for c in commands:
        op = c.split(" ")[0]
        polarity, value = c.split(" ")[1][0], int(c.split(" ")[1][1:])
        parsed_commands.append([op, polarity, value])
    return parsed_commands


def terminates(commands):
    done_commands = []
    acc = 0
    i = 0

    while i < len(commands):
        if i in done_commands:
            return False, acc

        done_commands.append(i)

        if commands[i][1] == "+":
            polarity = 1
        elif commands[i][1] == "-":
            polarity = -1
        else:
            print("Invalid polarity")

        if commands[i][0] == "nop":
            i += 1
        elif commands[i][0] == "acc":
            acc += commands[i][2] * polarity
            i += 1
        elif commands[i][0] == "jmp":
            i += commands[i][2] * polarity
        else:
            print("Invalid operation: ", commands[i][0])

    print(acc)
    return True, acc


def part1():
    commands = parse_commands(load_file())
    print(terminates(commands)[1])


def part2():
    commands = parse_commands(load_file())

    for i in range(len(commands)):
        if commands[i][0] == "jmp":
            commands[i][0] = "nop"
            if terminates(commands)[0]:
                break
            commands[i][0] = "jmp"

        elif commands[i][0] == "nop":
            commands[i][0] = "jmp"
            if terminates(commands)[0]:
                break
            commands[i][0] = "nop"
