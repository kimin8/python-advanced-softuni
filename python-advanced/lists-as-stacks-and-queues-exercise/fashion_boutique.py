clothes = [int(x) for x in input().split(" ")]
capacity = int(input())
stack = []
racks = 0
current_sum = 0

for i in range(len(clothes)):
    stack.append(clothes.pop())

while len(stack) > 0:
    last = stack.pop()

    if (current_sum + last) > capacity:
        racks += 1
        current_sum = last
    elif (current_sum + last) == capacity:
        racks += 1
        current_sum = 0
    else:
        current_sum += last
    
if current_sum > 0:
    print(racks + 1)
else:
    print(racks)