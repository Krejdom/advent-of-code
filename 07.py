def load_file(file_path="input.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def create_bag_dict():
    bag_dict = {}

    for rule in load_file():
        outer, inner = rule.split(" contain ")
        name = " ".join(outer.split(" ")[:2])

        content = []
        if inner != "no other bags.\n":
            for bag in inner.split(", "):
                quantity, kind, color, _ = bag.split(" ")
                inner_name = kind + " " + color
                content.append((int(quantity), inner_name))

        bag_dict[name] = content

    return bag_dict


def is_contained(searched_bag, bag_dict):
    can_be_in = []
    
    for name, content in bag_dict.items():
        for bag in content:
            _, inner_name = bag
            if searched_bag == inner_name:
                can_be_in.append(name)
    
    return can_be_in


def part1():
    bag_dict = create_bag_dict()
    can_be_in = []
    nxt_can_be_in = is_contained("shiny gold", bag_dict)

    while can_be_in != nxt_can_be_in:
        can_be_in = nxt_can_be_in
        for bag in can_be_in:
            nxt_can_be_in += is_contained(bag, bag_dict)

    print(len(set(nxt_can_be_in)))


def count_bags_inside(content, bag_dict):
    count = 0
    for bag in content:
        quantity, name = bag
        count += quantity * count_bags_inside(bag_dict[name], bag_dict) + 1
    return count


def part2():
    bag_dict = create_bag_dict()
    print(count_bags_inside(bag_dict["shiny gold"], bag_dict))
