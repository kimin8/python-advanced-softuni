from collections import deque

n = int(input())
road = deque()
current_petrol = 0
possible = []

for i in range(n):
    amount_of_petrol, distance_to_next = input().split(" ")
    amount_of_petrol = int(amount_of_petrol)
    distance_to_next = int(distance_to_next)
    road.append([amount_of_petrol, distance_to_next])

for i in range(len(road)):
    if road[0][0] + current_petrol < road[0][1]:
        road.rotate(-1)
    else:
        current_petrol += road[0][0] - road[0][1]
        possible.append(i)

print(min(possible))