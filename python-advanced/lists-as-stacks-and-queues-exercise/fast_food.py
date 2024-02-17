from collections import deque

quantity = int(input())
food_in_order = [int(x) for x in input().split(" ")]

line = deque(food_in_order)

print(max(food_in_order))

for i in range(len(line)):
    if line[0] <= quantity:
        quantity -= line[0]
        line.popleft()
    
    if len(line) == 0:
        print("Orders complete")
        break
else:
    print(f"Orders left: {' '.join([str(x) for x in line])}")