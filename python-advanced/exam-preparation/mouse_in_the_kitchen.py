rows, columns = [int(x) for x in input().split(",")]
matrix = []
current_position = []
last_known_position = []
total_cheese_in_matrix = 0

for r in range(rows):
    row_data = list(input())
    total_cheese_in_matrix += row_data.count("C")
    matrix.append(row_data)

for r in range(rows):
    for c in range(columns):
        if matrix[r][c] == "M":
            current_position = [r, c]

command = input()
while command != "danger":
    last_known_position = current_position.copy()
    if command == "up":
        if current_position[0] - 1 < 0:
            matrix[last_known_position[0]][last_known_position[1]] = "M"
            print("No more cheese for tonight!")
            break
        else:
            current_position[0] -= 1
    elif command == "down":
        if current_position[0] + 1 > rows - 1:
            matrix[last_known_position[0]][last_known_position[1]] = "M"
            print("No more cheese for tonight!")
            break
        else:
            current_position[0] += 1
    elif command == "left":
        if current_position[1] - 1 < 0:
            matrix[last_known_position[0]][last_known_position[1]] = "M"
            print("No more cheese for tonight!")
            break
        else:
            current_position[1] -= 1
    elif command == "right":
        if current_position[1] + 1 > columns - 1:
            matrix[last_known_position[0]][last_known_position[1]] = "M"
            print("No more cheese for tonight!")
            break
        else:
            current_position[1] += 1

    matrix[last_known_position[0]][last_known_position[1]] = "*"

    if matrix[current_position[0]][current_position[1]] == "C":
        matrix[current_position[0]][current_position[1]] = "M"
        total_cheese_in_matrix -= 1
        if total_cheese_in_matrix == 0:
            last_known_position = current_position.copy()
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[current_position[0]][current_position[1]] == "T":
        matrix[current_position[0]][current_position[1]] = "M"
        last_known_position = current_position.copy()
        print("Mouse is trapped!")
        break
    elif matrix[current_position[0]][current_position[1]] == "@":
        matrix[last_known_position[0]][last_known_position[1]] = "M"
        current_position = last_known_position.copy()

    command = input()

    if command == "danger" and total_cheese_in_matrix > 0:
        print("Mouse will come back later!")

for row in matrix:
    row_result = ""
    for element in row:
        row_result += element
    print(row_result)