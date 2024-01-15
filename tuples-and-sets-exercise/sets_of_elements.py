n, m = input().split(" ")
n = int(n)
m = int(m)

first_set = set()
second_set = set()

for i in range(n+m):
    if i < n:
        first_set.add(int(input()))
    else:
        second_set.add(int(input()))

for el in first_set:
    if el in second_set:
        print(el)
