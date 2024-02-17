n = int(input())

longest_range = []

for _ in range(n):
    range_of_nums = input()
    first, second = range_of_nums.split("-")
    first_tokens = first.split(",")
    second_tokens = second.split(",")

    first_start, first_end = map(int, first_tokens)
    second_start, second_end = map(int, second_tokens)

    x = range(first_start, first_end + 1)
    y = range(second_start, second_end + 1)

    intersection = range(max(x[0], y[0]), min(x[-1], y[-1])+1)
    length_of_intersection = min(x[-1], y[-1]) - max(x[0], y[0]) + 1
    if len(longest_range) == 0:
        longest_range = [intersection, length_of_intersection]
    else:
        if length_of_intersection > longest_range[1]:
            longest_range = [intersection, length_of_intersection]

to_print = map(str, list(longest_range[0]))

print(f"Longest intersection is [{', '.join(to_print)}] with length {longest_range[1]}")
