def load_input():
    with open("input.txt", "r") as f:
        return [int(i) for i in list(f.readlines()[0])]


class Cup():
    def __init__(self, label):
        self.label = int(label)
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.label)


class CupsCircle():
    def __init__(self, cups_list):
        self.current_cup = None
        self.cup_dict = {}
        self.min_cup = int(min(cups_list))
        self.max_cup = int(max(cups_list))

        for cup in cups_list:
            self.add_cup(cup)

        self.current_cup = self.current_cup.next

    def add_cup(self, label):
        cup = Cup(label)

        if not self.current_cup:
            cup.next = cup
            cup.prev = cup
            self.current_cup = cup
        else:
            tmp_cup = self.current_cup.next

            self.current_cup.next = cup
            cup.prev = self.current_cup

            tmp_cup.prev = cup
            cup.next = tmp_cup

            self.current_cup = cup

        self.cup_dict[label] = cup


    def put_3cups_after(self, three_cups, after_cup):
        before_cup = after_cup.next

        three_cups[0].prev = after_cup
        after_cup.next = three_cups[0]

        three_cups[2].next = before_cup
        before_cup.prev = three_cups[2]


    def remove_3cups(self, first):
        first.prev.next = first.next.next.next
        first.next.next.next.prev = first.prev

        return [first, first.next, first.next.next]


    def __str__(self):
        if not self.current_cup:
            return "Empty"

        output = "(" + str(self.current_cup.label) + ")"
        tmp_cup = self.current_cup.next

        while tmp_cup != self.current_cup:
            output += " " + str(tmp_cup.label)
            tmp_cup = tmp_cup.next
        return output


def get_destination(circle, three_labels):
    destination = circle.current_cup.label - 1

    if destination < circle.min_cup:
        destination = circle.max_cup

    while destination in three_labels:
        destination -= 1
        if destination < circle.min_cup:
            destination = circle.max_cup

    return circle.cup_dict[destination]


def play_round(circle):
    three_cups = circle.remove_3cups(circle.current_cup.next)
    three_labels = [cup.label for cup in three_cups]
    
    destination = get_destination(circle, three_labels)

    circle.put_3cups_after(three_cups, destination)

    circle.current_cup = circle.current_cup.next


def part1():
    circle = CupsCircle(load_input())

    for i in range(100):
        play_round(circle)
    print(circle)


def part2():
    cups = load_input() + [i for i in range(10, 1000001)]
    circle = CupsCircle(cups)

    for i in range(10000000):
        play_round(circle)

    tmp_cup = circle.current_cup
    while tmp_cup.label != 1:
        tmp_cup = tmp_cup.next

    print(tmp_cup.next.label * tmp_cup.next.next.label)    
