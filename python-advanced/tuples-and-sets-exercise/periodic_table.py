elements = set()
n = int(input())

for _ in range(n):
    compounds = input().split(" ")

    for el in compounds:
        elements.add(el)

print(*elements, sep="\n")
