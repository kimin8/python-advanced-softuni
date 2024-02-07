from collections import deque
initial_fuel = [int(x) for x in input().split(" ")]
additional_consumption_index = deque([int(x) for x in input().split(" ")])
amount_of_fuel_needed = deque([int(x) for x in input().split(" ")])

for n in range(1, len(initial_fuel) + 1):
    fuel_quantity_last = initial_fuel.pop()
    additional_consumption_first = additional_consumption_index.popleft()
    needed_amount_first = amount_of_fuel_needed.popleft()

    result_from_subtraction = fuel_quantity_last - additional_consumption_first
    if result_from_subtraction >= needed_amount_first:
        print(f"John has reached: Altitude {n}")
    else:
        print(f"John did not reach: Altitude {n}")
        if n > 1:
            altitudes = []
            for i in range(1, n):
                altitudes.append(f"Altitude {i}")
            print(f"John failed to reach the top.\nReached altitudes: {', '.join(altitudes)}")
        else:
            print("John failed to reach the top.\nJohn didn't reach any altitude.")
        exit()

print("John has reached all the altitudes and managed to reach the top!")