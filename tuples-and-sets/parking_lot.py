n = int(input())

cars = []

for i in range(n):
    command, car = input().split(", ")
    if command == "IN":
        cars.append(car)
    elif command == "OUT":
        cars.remove(car)

if len(cars) == 0:
    print("Parking Lot is Empty")
else:
    print(*set(cars), sep="\n")

