function read_input()
    open("02-input.txt") do file
        total_score = 0

        lines = readlines(file)
        for l in lines
            l = split(l, " ")

            if l[2] == "X"
                if l[1] == "A"
                    total_score += 3
                elseif l[1] == "B"
                    total_score += 1
                elseif l[1] == "C"
                    total_score += 2
                end
            elseif l[2] == "Y"
                total_score += 3
                if l[1] == "A"
                    total_score += 1
                elseif l[1] == "B"
                    total_score += 2
                elseif l[1] == "C"
                    total_score += 3
                end
            elseif l[2] == "Z"
                total_score += 6
                if l[1] == "A"
                    total_score += 2
                elseif l[1] == "B"
                    total_score += 3
                elseif l[1] == "C"
                    total_score += 1
                end
            end

            println(total_score)
        end
    end
end

read_input()
