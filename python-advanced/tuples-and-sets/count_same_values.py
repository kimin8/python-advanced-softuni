numbers = input().split(" ")

occurrences = {}

nums = [float(x) for x in numbers]

for x in nums:
    if x in occurrences.keys():
        occurrences[x] += 1
    else:
        occurrences[x] = 1

for key in occurrences.keys():
    print(f"{key:.1f} - {occurrences[key]} times")
