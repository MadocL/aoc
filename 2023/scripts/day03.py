input_ = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

input_ = open('day03.txt', 'r', encoding='utf-8').read().splitlines()

valid_list = []
number = False
valid = False
geart_part = False
current_number = ""
gears = {}

for i in range(len(input_)):
    line = input_[i]
    for j in range(len(line)):
        if line[j] == "*" and str(i) + "," + str(j) not in gears:
            gears[str(i) + "," + str(j)] = []
        if line[j].isdigit():
            number = True
            current_number += line[j]

            neighbors = [
                (i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1),             (i, j+1),
                (i+1, j-1), (i+1, j), (i+1, j+1),
            ]
            for ni, nj in neighbors:
                if 0 <= ni < len(input_) and 0 <= nj < len(line):
                    if input_[ni][nj] in "*+#$%/&@=-":
                        if input_[ni][nj] == "*":
                            gear_part = True
                            if str(ni) + "," + str(nj) not in gears:
                                gears[str(ni) + "," + str(nj)] = []
                            last_gear_pos = str(ni) + "," + str(nj)
                        valid = True
                        break
        else:
            number = False
            if valid:
                valid_list.append(int(current_number))
                if gear_part:
                    gears[last_gear_pos].append(int(current_number))
                    gear_part = False
            valid = False
            current_number = ""
    if valid:
        number = False
        valid_list.append(int(current_number))
        if gear_part:
            gears[last_gear_pos].append(int(current_number))
            gear_part = False
        valid = False
        current_number = ""


print(valid_list, sum(valid_list))

gear_ration_sum = 0
for gear_pos, gear_parts in gears.items():
    if len(gear_parts) == 2:
        gear_ration_sum += gear_parts[0] * gear_parts[1]
print(gears)
print(gear_ration_sum)
