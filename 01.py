def load_report():
    report = []

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            report.append(int(line.strip()))

    return report


def part_1():
    report = load_report()
    for i in range(len(report) - 1):
        for j in range(i, len(report)):
            if report[i] + report[j] == 2020:
                print(report[i] * report[j])


def part_2():
    report = load_report()

    for i in range(len(report) - 2):
        for j in range(i, len(report) - 1):
            for k in range(j, len(report)):
                if report[i] + report[j] + report[k] == 2020:
                    print(report[i] * report[j] * report[k])


if __name__ == '__main__':
    part_1()
    part_2()
