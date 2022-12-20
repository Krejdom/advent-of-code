function read_input()
    open("04-input.txt") do file
        lines = readlines(file)
        return lines
    end
end

function part1()
    sum_containing = 0
    for line in read_input()
        assignments = split(line, ",")
        elf1 = split(assignments[1], "-")
        elf2 = split(assignments[2], "-")

        if parse(Int, elf1[1]) <= parse(Int, elf2[1]) && parse(Int, elf1[2]) >= parse(Int, elf2[2])
            sum_containing += 1
            println(elf1, "--", elf2)
        elseif parse(Int, elf1[1]) >= parse(Int, elf2[1]) && parse(Int, elf1[2]) <= parse(Int, elf2[2])
            sum_containing += 1
            println(elf1, "--", elf2)
        end
    end
    return sum_containing
end

function part2()
    sum_containing = 0
    for line in read_input()
        assignments = split(line, ",")
        elf1 = split(assignments[1], "-")
        elf2 = split(assignments[2], "-")

        if parse(Int, elf1[1]) >= parse(Int, elf2[1]) && parse(Int, elf1[1]) <= parse(Int, elf2[2])
            sum_containing += 1
            println(elf1, "--", elf2)
        elseif parse(Int, elf1[2]) >= parse(Int, elf2[1]) && parse(Int, elf1[2]) <= parse(Int, elf2[2])
            sum_containing += 1
            println(elf1, "--", elf2)
        elseif parse(Int, elf2[1]) >= parse(Int, elf1[1]) && parse(Int, elf2[1]) <= parse(Int, elf1[2])
            sum_containing += 1
            println(elf1, "--", elf2)
        elseif parse(Int, elf2[2]) >= parse(Int, elf1[1]) && parse(Int, elf2[2]) <= parse(Int, elf1[2])
            sum_containing += 1
            println(elf1, "--", elf2)
        end
    end
    return sum_containing
end

#println(part1())
println(part2())
