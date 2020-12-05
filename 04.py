import re


def load_passports():
    passports = []

    with open("input.txt", "r", encoding="utf-8") as f:
        passport = {}
        for line in f:
            if line == "\n":
                passports.append(passport)
                passport = {}
                continue

            for d in line.strip().split(" "):
                k, v = d.split(":")
                passport[k] = v

        passports.append(passport)

    return passports


def contains_all_fields(passport):
    for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if k not in passport:
            return False
    return True


def height_is_ok(passport):
    if "cm" in passport["hgt"]:
        height = int(passport["hgt"][:-2])
        return height >= 150 and height <= 193

    elif "in" in passport["hgt"]:
        height = int(passport["hgt"][:-2])
        return height >= 59 and height <= 76

    else:
        return False


def is_valid(passport):
    if not contains_all_fields(passport):
        return False

    if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False

    if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False

    if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False

    if not height_is_ok(passport):
        return False

    # https://stackoverflow.com/questions/30241375/python-how-to-check-if-string-is-a-hex-color-code
    if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport["hcl"]):
        return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if len(passport["pid"]) != 9 or not passport["pid"].isdecimal():
        return False

    return True


def part1():
    passports = load_passports()
    valid_passports = 0
    for passport in passports:
        if contains_all_fields(passport):
            valid_passports += 1

    print(valid_passports)


def part2():
    passports = load_passports()
    valid_passports = 0
    for passport in passports:
        if is_valid(passport):
            valid_passports += 1

    print(valid_passports)
