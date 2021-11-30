def load_file(file_path="input.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def get_all_answers():
    loaded_file = load_file()
    all_groups_answers = []
    group_answers, n_respondents = {}, 0

    for line in loaded_file:
        if line == "\n":
            all_groups_answers.append((n_respondents, group_answers))
            group_answers, n_respondents = {}, 0

        else:
            for a in line.strip():
                if a not in group_answers:
                    group_answers[a] = 1
                else:
                    group_answers[a] += 1
            n_respondents += 1
    all_groups_answers.append((n_respondents, group_answers))

    return all_groups_answers


def part1():
    count = 0
    for _, answers in get_all_answers():
        count += len(answers)
    print(count)


def part2():
    count = 0
    for n_respondents, answers in get_all_answers():
        for key, value in answers.items():
            if value == n_respondents:
                count += 1
    print(count)
