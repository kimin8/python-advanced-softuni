from collections import deque

person = input()
line = deque([])

while person != "End":
    if person != "Paid":
        line.append(person)
    else:
        for x in line:
            print(x)
        line.clear()
    
    person = input()
    
print(f"{len(line)} people remaining.")