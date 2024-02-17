n = int(input())
codes = set()

for _ in range(n):
    code = input()
    codes.add(code)

name = input()
while name != "END":
    if name in codes:
        codes.remove(name)
    name = input()

print(len(codes))
for code in sorted(codes):
    print(code)
