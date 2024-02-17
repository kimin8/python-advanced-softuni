n = int(input())

matrix = []
jet_position = []
enemies_count = 0
armor_value = 300

for row in range(n):
    data = list(input())
    enemies_count += data.count("E")
    matrix.append(data)

    for col in range(n):
        if data[col] == "J":
            jet_position = [row, col]

command = input()
while enemies_count > 0 and armor_value > 0:
    last_position = jet_position.copy()
    if command == "up":
        jet_position[0] -= 1
    elif command == "down":
        jet_position[0] += 1
    elif command == "left":
        jet_position[1] -= 1
    elif command == "right":
        jet_position[1] += 1

    current_symbol = matrix[jet_position[0]][jet_position[1]]

    if current_symbol == "-":
        matrix[jet_position[0]][jet_position[1]] = "J"
        matrix[last_position[0]][last_position[1]] = "-"
    elif current_symbol == "E":
        if enemies_count == 1:
            enemies_count -= 1
            matrix[jet_position[0]][jet_position[1]] = "J"
            matrix[last_position[0]][last_position[1]] = "-"
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor_value -= 100
            matrix[jet_position[0]][jet_position[1]] = "J"
            matrix[last_position[0]][last_position[1]] = "-"
            enemies_count -= 1
            if armor_value == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_position[0]}, {jet_position[1]}]!")
                break
    elif current_symbol == "R":
        armor_value = 300
        matrix[jet_position[0]][jet_position[1]] = "J"
        matrix[last_position[0]][last_position[1]] = "-"

    command = input()

for row in matrix:
    curr_row = ""
    for el in row:
        curr_row += el
    print(curr_row)
