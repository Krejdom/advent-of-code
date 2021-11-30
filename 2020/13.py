def load_file(file_path="input.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return int(lines[0].strip()), lines[1].strip().split(",")


def part1():
    departures = {}
    earliest_timestamp, buses = load_file()

    min_bus = None
    min_bus_dep = float("inf")
    for bus in buses:
        if bus == "x":
            pass
        else:
            bus = int(bus)
            bus_departure = (earliest_timestamp // bus) * bus
            if bus_departure != earliest_timestamp:
                bus_departure += bus

            if min_bus_dep > bus_departure:
                min_bus, min_bus_dep = bus, bus_departure

    print(min_bus * (min_bus_dep - earliest_timestamp))


def part2():
    """Prints an equation which I put in https://www.wolframalpha.com/"""
    _, buses = load_file()
    parameter = 0
    for bus in buses:
        if bus == "x":
            pass
        else:
            print("(y +", parameter, ") mod", bus," = 0,")
        parameter += 1


def is_solution(t, buses):
    """Checks if time t is a solution."""
    parameter = 0
    for bus in buses:
        if bus == "x":
            pass
        else:
            if (t + parameter) % int(bus) != 0:
                return False
        parameter += 1

    return True
