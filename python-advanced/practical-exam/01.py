from collections import deque

amount_of_money = [int(x) for x in input().split(" ")]
price_size = deque([int(x) for x in input().split(" ")])
initial_length_of_prices = len(price_size)
food_count = 0

while len(amount_of_money) > 0 and len(price_size) > 0:
    current_amount_of_money = amount_of_money.pop()
    current_price_size = price_size.popleft()

    if current_amount_of_money == current_price_size:
        food_count += 1
    elif current_amount_of_money > current_price_size:
        food_count += 1
        change = current_amount_of_money - current_price_size
        if amount_of_money:
            amount_of_money[-1] += change
            
if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif initial_length_of_prices > len(price_size):
    if food_count > 1:
        print(f"Henry ate: {food_count} foods.")
    elif food_count == 1:
        print(f"Henry ate: {food_count} food.")

if food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
