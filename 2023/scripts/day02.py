input_ = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
input_ = open('day02.txt', 'r', encoding='utf-8').read().splitlines()

games = []
for line in input_:
    id_ = int(line.split(': ')[0].split(' ')[1])
    sets = []

    for set_ in line.split(': ')[1].split('; '):
        sets.append({cube.split(" ")[1]: int(cube.split(" ")[0]) for cube in set_.split(", ")})

    games.append((id_, sets))

# for game in games:
#     print(game[0])
#     for set_ in game[1]:
#         print('\t' + str(set_))

sum_ = 0
for id_, sets in games:
    print(id_, sets)
    possible = True
    for set_ in sets:
        if (
            "red" in set_ and set_["red"] > 12 or
            "green" in set_ and set_["green"] > 13 or
            "blue" in set_ and set_["blue"] > 14
        ):
            possible = False
            break
    if possible:
        sum_ += id_
print(sum_)

# part 2
sum_ = 0
for id_, sets in games:
    max_red = 0
    max_green = 0
    max_blue = 0
    for set_ in sets:
        if "red" in set_ and set_["red"] > max_red:
            max_red = set_["red"]
        if "green" in set_ and set_["green"] > max_green:
            max_green = set_["green"]
        if "blue" in set_ and set_["blue"] > max_blue:
            max_blue = set_["blue"]
    sum_ += max_red * max_green * max_blue
print(sum_)
