nums = [x for x in input().split(" ")]
stack = []

for i in range(0, len(nums)):
    stack.append(nums.pop())

print(" ".join(stack))