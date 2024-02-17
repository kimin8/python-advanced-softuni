n = int(input())

matrix = []
bank_account = 100

for row in range(n):
    data = [x for x in list(input())]
    matrix.append(data)

current_position = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == "G":
            current_position = [r, c]

command = input()

while command != "end":
    matrix[current_position[0]][current_position[1]] = "-"

    if command == "up":
        if current_position[0] - 1 < 0:
            matrix[current_position[0]][current_position[1]] = "G"
            print("Game over! You lost everything!")
            exit()
        else:
            current_position[0] -= 1
    elif command == "down":
        if current_position[0] + 1 > n - 1:
            matrix[current_position[0]][current_position[1]] = "G"
            print("Game over! You lost everything!")
            exit()
        else:
            current_position[0] += 1
    elif command == "left":
        if current_position[1] - 1 < 0:
            matrix[current_position[0]][current_position[1]] = "G"
            print("Game over! You lost everything!")
            exit()
        else:
            current_position[1] -= 1
    elif command == "right":
        if current_position[1] + 1 > n - 1:
            matrix[current_position[0]][current_position[1]] = "G"
            print("Game over! You lost everything!")
            exit()
        else:
            current_position[1] += 1
    
    new_position = matrix[current_position[0]][current_position[1]]

    if new_position == "W":
        bank_account += 100
    elif new_position == "P":
        bank_account -= 200
        if bank_account <= 0:
            matrix[current_position[0]][current_position[1]] = "G"
            print("Game over! You lost everything!")
            exit()
    elif new_position == "J":
        bank_account += 100000
        print(f"You win the Jackpot! End of the game. Total amount: {bank_account}$")
        exit()

    matrix[current_position[0]][current_position[1]] = "G"

    command = input()

print(f"End of the game. Total amount: {bank_account}$")

for row in matrix:
    row_data = ""
    for el in row:
        row_data += el
    print(row_data)