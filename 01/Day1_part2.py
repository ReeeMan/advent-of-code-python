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


similarity_score = 0
for locationID in left_column:

    occurrences = right_column.count(locationID)
    similarity_score += locationID * occurrences

print(similarity_score)
