def load_calibration_document():
    doc = []

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            doc.append(line.strip())

    return doc


def part_1():
    cal_val_sum = 0
    doc = load_calibration_document()
    for line in doc:
        # https://www.geeksforgeeks.org/python-extract-numbers-from-string/
        nums = [int(i) for i in line if i.isdigit()]
        cal_val = nums[0]*10 + nums[-1]
        cal_val_sum += cal_val
    print(cal_val_sum)


def part_2():
    doubles = {
        "oneight"   : "oneeight",
        "twone"     : "twoone",
        "threeight" : "threeeight",
        "fiveight"  : "fiveeight",
        "sevenine"  : "sevennine",
        "eightwo"   : "eighttwo",
        "eighthree" : "eightthree",
        "nineight"  : "nineeight",
    }

    nums_digits = {
        "one"   : "1",
        "two"   : "2",
        "three" : "3",
        "four"  : "4",
        "five"  : "5",
        "six"   : "6",
        "seven" : "7",
        "eight" : "8",
        "nine"  : "9",
    }

    cal_val_sum = 0
    doc = load_calibration_document()

    for line in doc:
        for double, doubled in doubles.items():
            line = line.replace(double, doubled)
        for num, digit in nums_digits.items():
            line = line.replace(num, digit)
            nums = [int(i) for i in line if i.isdigit()]
        cal_val = nums[0]*10 + nums[-1]
        cal_val_sum += cal_val

    print(cal_val_sum)


if __name__ == '__main__':
    part_1()
    part_2()
