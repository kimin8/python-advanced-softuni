n = int(input())
QUOTA = 20

matrix = []
for row in range(n):
    matrix.append(list(input()))

total_fish = 0

current_position = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "S":
            current_position = [row, col]
            break

last_symbol = '-'

command = input()
while command != "collect the nets":
    matrix[current_position[0]][current_position[1]] = last_symbol
    if command == "up":
        if (current_position[0] - 1) < 0:
            current_position[0] = n - 1
        else:
            current_position = [current_position[0] - 1, current_position[1]]
    elif command == "down":
        if (current_position[0] + 1) > (n - 1):
            current_position[0] = 0
        else:
            current_position = [current_position[0] + 1, current_position[1]]
    elif command == "left":
        if (current_position[1] - 1) < 0:
            current_position[1] = n - 1
        else:
            current_position = [current_position[0], current_position[1] - 1]
    elif command == "right":
        if (current_position[1] + 1) > (n - 1):
            current_position[1] = 0
        else:
            current_position = [current_position[0], current_position[1] + 1]
    
    spot = matrix[current_position[0]][current_position[1]]

    if spot.isdigit():
        total_fish += int(spot)
        matrix[current_position[0]][current_position[1]] = '-'
    elif spot == 'W':
        total_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{current_position[0]},{current_position[1]}]")
        matrix[current_position[0]][current_position[1]] = 'S'
        exit()
    
    matrix[current_position[0]][current_position[1]] = 'S'
    
    command = input()

if total_fish >= QUOTA:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - total_fish} tons of fish more.")

if total_fish > 0:
    print(f"Amount of fish caught: {total_fish} tons.")

for row in matrix:
    to_print = ""
    for el in row:
        to_print += el
    print(to_print)
