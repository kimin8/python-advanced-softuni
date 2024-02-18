import os

user_input = input()

path = os.path.join('C:\\', 'Users', 'KimiNikolov', 'Desktop', 'python-advanced-softuni', 'python-advanced', 'file-handling-exercise', user_input)
files = {}
folders = []
for item in os.listdir(path):
    if "." in item:
        name, extension = item.split(".")
        if name in files.keys():
            files[name].append(item)
        else:
            files[name] = [item]
    else:
        folders.append(item)

report = ""
report += "============================"
report += "\nFolders:"

for folder in folders:
    report += f"\n\t** {folder}"
report += "\n============================"
report += "\nFiles:"

for file_name in files.keys():
    report += f"\n\t** {files[file_name][0]}"

report += "\n============================"

with open("report.txt", "w") as file:
    file.write(report)