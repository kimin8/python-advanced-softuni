n = int(input())

names = []

for i in range(n):
    name = input()
    names.append(name)

unique = {x for x in names}
for r in unique:
    print(r)
