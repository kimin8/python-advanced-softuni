sequence_one = set(map(int, input().split(" ")))
sequence_two = set(map(int, input().split(" ")))

n = int(input())

for _ in range(n):
    commands = input().split(" ")

    if "Add" in commands and "First" in commands:
        user_input = map(int, commands[2:])
        sequence_one.update(user_input)
    elif "Add" in commands and "Second" in commands:
        user_input = map(int, commands[2:])
        sequence_two.update(user_input)
    elif "Remove" in commands and "First" in commands:
        user_input = map(int, commands[2:])
        sequence_one.difference_update(user_input)
    elif "Remove" in commands and "Second" in commands:
        user_input = map(int, commands[2:])
        sequence_two.difference_update(user_input)
    elif "Check" in commands:
        x = sequence_one.issubset(sequence_two)
        y = sequence_two.issubset(sequence_one)

        if x or y:
            print(True)
        else:
            print(False)

sequence_one = sorted(sequence_one)
sequence_two = sorted(sequence_two)

print(*sequence_one, sep=", ")
print(*sequence_two, sep=", ")