def load_input():
    doc = []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            win, tip = line.split(": ")[1].split(" | ")
            win = set([int(n.strip()) for n in win.split()])
            tip = [int(n.strip()) for n in tip.split()]
            doc.append((win, tip))
    return doc


def count_wins(win, tips):
    wins = 0
    for tip in tips:
        if tip in win:
            wins += 1
    return wins


def part_1():
    total_points = 0
    cards = load_input()

    for card in cards:
        win, tip = card
        wins = count_wins(win, tip)
        points = wins * 2 if wins > 2 else wins
        total_points += points
    print(total_points)


def part_2():
    cards = load_input()
    owned_cards = [1 for i in range(len(cards))]

    n = 0
    for card in cards:
        win, tip = card
        matches = count_wins(win, tip)
        for i in range(matches):
            owned_cards[n+i+1] += 1 * owned_cards[n]
        n += 1

    print(sum(owned_cards))


if __name__ == '__main__':
    part_1()
    part_2()
