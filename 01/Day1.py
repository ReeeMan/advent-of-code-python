#create 2 column lists
left_column = []
right_column = []

##Load Puzzle input
file_path = "Puzzle Input.txt"
with open(file_path, "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_column.append(left)
        right_column.append(right)


#sort the lists lowest -> highest to make comparing easier
left_column.sort()
right_column.sort()

#zip
#combines 2 lists into pairs
#1st element of left_column and 1st element of right_column
differences = []
for left, right in zip(left_column, right_column):
    differences.append(abs(left - right))

print(differences)
#loop through differences and add them together to get totaldist (solution)
totalDist = 0
for difference in differences:
    totalDist = totalDist + difference


print(totalDist)
