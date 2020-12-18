BIT = 36


def load_file(file_path="input.txt"):
    instructions = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            instructions.append(line.strip().split(" = "))

    return instructions


def sum_memory(memory):
    result = 0
    for address, value in memory.items():
        result += int(value, 2)

    return result


def apply_mask_value(mask, value):
    new_value = ""

    for i in range(BIT):
        if mask[i] == "X":
            new_value += value[i]
        else:
            new_value += mask[i]

    return new_value


def address_value_init(instruction, memory):
    address = instruction[0][4:-1]

    if address not in memory:
        memory[address] = "0" * BIT

    value = "{0:b}".format(int(instruction[1]))
    while len(value) < BIT:
        value = "0" + value 

    return address, value, memory


def part1():
    memory = {}
    instructions = load_file()
    mask = None

    for instruction in instructions:
        if instruction[0] == "mask":
            mask = instruction[1]
        else:
            address, value, memory = address_value_init(instruction, memory)
            memory[address] = apply_mask_value(mask, value)

    print(sum_memory(memory))


def apply_mask_address(mask, address):
    new_address = ""

    for i in range(BIT):
        if mask[i] == "1":
            new_address += mask[i]
        else:
            new_address += address[i]

    return new_address


def create_addresses(mask, address, memory):
    all_addresses = []

    if "X" not in mask:
        all_addresses.append(apply_mask_address(mask, address))
    else:
        x_index = mask.index("X")
        mask = mask.replace("X", "0", 1)
        address_list = list(address)

        address_list[x_index] = "0"
        new_address = "".join(address_list)
        all_addresses += create_addresses(mask, new_address, memory)
        
        address_list[x_index] = "1"
        new_address = "".join(address_list)
        all_addresses += create_addresses(mask, new_address, memory)

    return all_addresses


def part2():
    memory = {}
    instructions = load_file()
    mask = None

    for instruction in instructions:
        if instruction[0] == "mask":
            mask = instruction[1]
        else:
            address, value, memory = address_value_init(instruction, memory)
            prefix = "0" * (BIT - len("{0:b}".format(int(address))))
            bin_address = prefix + "{0:b}".format(int(address))

            new_addresses = create_addresses(mask, bin_address, memory)

            for a in new_addresses:
                memory[a] = value

    print(sum_memory(memory))
