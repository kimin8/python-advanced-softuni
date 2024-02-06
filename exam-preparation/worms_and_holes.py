from collections import deque
worm_size = [int(x) for x in input().split(" ")]
start_len = len(worm_size)
hole_size = deque([int(x) for x in input().split(" ")])

matches = 0

while len(worm_size) > 0 and len(hole_size) > 0:
    worm = worm_size.pop()
    hole = hole_size.popleft()
    
    if worm != hole:
        worm -= 3
        if worm > 0:
            worm_size.append(worm)
    else:
        matches += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if len(worm_size) == 0 and matches == start_len:
    print("Every worm found a suitable hole!")
elif len(worm_size) == 0 and matches < start_len:
    print("Worms left: none")
elif len(worm_size) > 0:
    print(f"Worms left: {', '.join([str(x) for x in worm_size])}")

if len(hole_size) == 0:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in hole_size])}")