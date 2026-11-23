input_ = [
    "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four",
    "4nineeightseven2", "zoneight234", "7pqrstsixteen",
]
input_ = open('day01.txt', 'r', encoding='utf-8').readlines()
# print(input_)

sum_ = 0
numbers = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
for line in input_:
    reversed_line = line[::-1]
    mini_index = len(line)
    maxi_index = -1
    for i in range(len(numbers)):
        index = line.find(numbers[i])
        if index != -1:
            if index < mini_index:
                mini_index = index
                mini_number_index = i
            last_match_index = reversed_line.find(numbers[i][::-1])
            if len(line) - last_match_index > maxi_index:
                maxi_index = len(line) - last_match_index
                maxi_number_index = i

    if mini_number_index > 8:
        first_digit = numbers[mini_number_index - 9]
    else:
        first_digit = numbers[mini_number_index]
    if maxi_number_index > 8:
        second_digit = numbers[maxi_number_index - 9]
    else:
        second_digit = numbers[maxi_number_index]
    number_to_add = int(first_digit + second_digit)
    sum_ += number_to_add
    print(line, numbers[mini_number_index], numbers[maxi_number_index], number_to_add)
print(sum_)
