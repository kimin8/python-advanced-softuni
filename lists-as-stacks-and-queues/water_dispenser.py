from collections import deque
quantity = int(input())

name = input()
line = deque()

while name != "Start":
    line.append(name)
    name = input()

command = input()

while command != "End":
    if "refill" in command:
        _, to_add = command.split(" ")
        quantity += int(to_add)
    else:
        liters = int(command)
        if liters <= quantity:
            quantity -= liters
            print(f"{line.popleft()} got water")
        else:
            print(f"{line.popleft()} must wait")

    command = input()

print(f"{quantity} liters left")