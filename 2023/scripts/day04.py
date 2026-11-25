from utils.load_inputs import load_file
from utils.pretty_printing import line_by_line_print


def part1(inputs) -> int:
    global_score = 0
    for _, winning_numbers, numbers in inputs:
        score = 0
        for nb in numbers:
            if nb in winning_numbers:
                if score >= 1:
                    score *= 2
                else:
                    score += 1
        global_score += score
    return global_score


def part2(inputs) -> int:
    won_cards_count = [0] * len(inputs)

    for card_number, winning_numbers, numbers in inputs:
        matching_numbers_count = 0
        for nb in numbers:
            if nb in winning_numbers:
                matching_numbers_count += 1
        for i in range(card_number + 1, card_number + 1 + matching_numbers_count):
            won_cards_count[i - 1] += 1 + won_cards_count[card_number - 1]
    return len(inputs) + sum(won_cards_count)


FILENAME = "day04.txt"
# FILENAME = "day04_s.txt"

parsed_inputs = [
    (
        int(line.split(": ")[0].split(" ")[-1]),
        [int(nb) for nb in line.split(": ")[1].split(" | ")[0].split(" ") if nb != ""],
        [int(nb) for nb in line.split(": ")[1].split(" | ")[1].strip().split(" ") if nb != ""],
    )
    for line in load_file("2023/inputs/", FILENAME)
]

line_by_line_print(parsed_inputs)
print(part1(parsed_inputs))
print(part2(parsed_inputs))
