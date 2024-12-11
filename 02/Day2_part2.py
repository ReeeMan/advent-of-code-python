# create 2 column lists
reports = []

##Load Puzzle input
file_path = "Puzzle Input.txt"
with open(file_path, "r") as file:
    for line in file:
        reports.append([int(x) for x in line.split()])


def follows_rules(nums):
    # Check if the list is increasing or decreasing
    is_increasing = True
    is_decreasing = True
    valid_difference = True

    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            is_increasing = False
        if nums[i] <= nums[i + 1]:
            is_decreasing = False
        if is_increasing or is_decreasing:  # only need to check here if list is actually increasing/decreasing
            if not (1 <= abs(nums[i] - nums[i + 1]) <= 3):
                valid_difference = False
                break

    return (is_increasing or is_decreasing) and valid_difference


valid_counter = 0

for report in reports:
    if follows_rules(report):
        valid_counter = valid_counter + 1
    else:  # anything that doesnt follow the rules try again but shift through the numbers removing 1 at a time.
        # print out the fixed values because its interesting to see
        for i in range(len(report)):
            temp_numbers = report[:i] + report[i + 1:]
            if follows_rules(temp_numbers):
                valid_counter = valid_counter + 1
                print('[VALID with Dampener fix] numbers - ' + str(report) + ' | temp_numbers ' + str(temp_numbers))
                break

print('Solution : ' + str(valid_counter))
