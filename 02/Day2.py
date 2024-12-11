#create 2 column lists
reports = []

##Load Puzzle input
file_path = "Puzzle Input.txt"
with open(file_path, "r") as file:
    for line in file:
        reports.append([int(x) for x in line.split()])

#investigate "all" function

valid_counter = 0
for report in reports:
    first_number = ''

    is_increasing = True
    is_decreasing = True
    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            is_increasing = False
        if report[i] <= report[i + 1]:
            is_decreasing = False

    if is_increasing or is_decreasing:
        valid_difference = True
        for i in range(len(report) - 1):
            if not (1 <= abs(report[i] - report[i + 1]) <= 3):
                valid_difference = False
                break
        if valid_difference:
            valid_counter = valid_counter + 1




print(valid_counter)
