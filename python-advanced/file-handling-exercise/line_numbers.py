import os
path = os.path.abspath("text.txt")
symbols = (".", "?", "!", "-", "\"", ",", "(", ")", "'", ":", ";", "`")
try:
    file = open(path, 'r')
    new_file = open("output.txt", "w")
    result = []
    lines = file.readlines()
    for index in range(0, len(lines)):
        punctuation_count = 0
        letter_count = 0
        current_line = lines[index]
        for letter in current_line:
            if letter.isalpha():
                letter_count += 1
            elif letter in symbols:
                punctuation_count += 1
        result.append(f"Line {index + 1}: {lines[index].strip()} ({letter_count})({punctuation_count})")
        
    new_file.write("\n".join(result))

except FileNotFoundError:
    print("File not found")
except FileExistsError:
    print("File already exists in the directory")