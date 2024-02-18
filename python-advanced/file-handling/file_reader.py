sum = 0
try:
    file = open('C:\\Users\\KimiNikolov\\Desktop\\python-advanced-softuni\\python-advanced\\file-handling\\numbers.txt', 'r')
    for line in file.readlines():
        sum += int(line)
    print(sum)
except FileNotFoundError:
    print("File not found")