function read_input()
    open("03-input.txt") do file
        lines = readlines(file)
        return lines
    end
end

function letter_to_num(l)
    priority = Int(l) - 96
    if priority < 1
        priority += 58
    end
    return priority
end

function find_duplicate(s)
    l = length(s)
    half_size = convert(Int64, l / 2)
    first_half = SubString(s, 1:half_size)
    second_half = SubString(s, half_size+1:l)
    return letter_to_num(intersect(first_half, second_half)[1])
end

function part1()
    priority_sum = 0
    for line in read_input()
        priority_sum += find_duplicate(line)
    end
    return priority_sum
end

function part2()
    priority_sum = 0
    rucksacks = read_input()
    rucksacks_count = length(rucksacks)
    i = 1
    while i <= rucksacks_count
        priority_sum += letter_to_num(intersect(rucksacks[i], rucksacks[i+1], rucksacks[i+2])[1])
        i += 3
    end
    return priority_sum
end

println(part2())
