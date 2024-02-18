import os

command = input()
while command != "End":
    tokens = command.split("-")
    if tokens[0] == "Create":
        _, file_name = tokens
        open(file_name, 'w')
    elif tokens[0] == "Add":
        _, file_name, content = tokens
        with open(file_name, "a") as file:
            file.write(content + "\n")
    elif tokens[0] == "Replace":
        _, file_name, old_string, new_string = tokens
        try:
            file = open(file_name, "r")
            lines = file.readlines()
            with open(file_name, 'w') as file:
                for i in range(0, len(lines)):
                    if old_string in lines[i]:
                        lines[i] = lines[i].replace(old_string, new_string)
                    file.write(lines[i])
        except FileNotFoundError:
            print("An error occurred")
    elif tokens[0] == "Delete":
        _, file_name = tokens
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
                    
    command = input()