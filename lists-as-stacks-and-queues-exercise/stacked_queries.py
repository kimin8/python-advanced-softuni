n = int(input())
stack = []

for i in range(n):
    command = input()

    if '1' in command:
        _, number = command.split(" ")
        stack.append(int(number))
    elif command == '2':
        if len(stack) > 0:
            stack.pop()
    elif command == '3':
        if len(stack) > 0:
            print(max(stack))
    elif command == '4':
        if len(stack) > 0:
            print(min(stack))

print(", ".join([str(x) for x in stack][::-1]))