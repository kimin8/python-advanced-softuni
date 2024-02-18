import os
path = os.path.join('text.txt')

chars_to_replace = ("-", ",", ".", "!", "?")

try:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(0, len(lines)):
        if i % 2 == 0:
            for symbol in chars_to_replace:
                lines[i] = lines[i].replace(symbol, "@")
            print(*lines[i].split()[::-1])
except FileNotFoundError:
    print("File not found")