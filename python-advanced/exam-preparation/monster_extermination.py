from collections import deque

armor_values = deque([int(x) for x in input().split(",")])
striking_impact = [int(x) for x in input().split(",")]
monsters_killed = 0

while len(armor_values) > 0 and len(striking_impact) > 0:
    first_armour_value = armor_values.popleft()
    last_striking_value = striking_impact.pop()

    if last_striking_value >= first_armour_value:
        monsters_killed += 1
        last_striking_value -= first_armour_value
        
        if len(striking_impact) > 0:
                striking_impact[-1] += last_striking_value
        else:
            if last_striking_value > 0:
                striking_impact.append(last_striking_value)
    else:
        first_armour_value -= last_striking_value
        armor_values.append(first_armour_value)

if not armor_values:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")