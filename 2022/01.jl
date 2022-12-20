function part1()
    open("01-input.txt") do file
        max_cal = 0
        current_elf = 0
        lines = readlines(file)
        for l in lines
            print(l)
            print("\n")
            if l == ""
                if current_elf > max_cal
                    max_cal = current_elf
                end
                current_elf = 0
            else
                current_elf += parse(Int64, l)
            end
        end
    print(max_cal)
    end
end

part1()


function part2()
    open("01-input.txt") do file
        max_cal = 0
        current_elf = 0
        max_cal2 = 0
        max_cal3 = 0
        lines = readlines(file)

        for l in lines
            if l != ""
                current_elf += parse(Int64, l)
                print(l, " ", current_elf, "\n")
            else
                if current_elf > max_cal
                    max_cal3 = max_cal2
                    max_cal2 = max_cal
                    max_cal = current_elf
                elseif current_elf > max_cal2
                    max_cal3 = max_cal2
                    max_cal2 = current_elf
                elseif current_elf > max_cal3
                    max_cal3 = current_elf
                end
                current_elf = 0
                print("\n")
                print("*", max_cal, " ", max_cal2, " ", max_cal3, "*")
                print("\n\n")
            end
        end
    print(max_cal, " ", max_cal2, " ", max_cal3)
    print("\n")
    print(max_cal + max_cal2 + max_cal3)
    end
end

part2()
