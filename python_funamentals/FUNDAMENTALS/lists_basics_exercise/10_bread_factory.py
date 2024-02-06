total_energy = 100
total_coins = 100
work_day_events = input().split("|")
bakery_is_open = True

for event in work_day_events:
    event_or_ingredient, number = event.split("-")
    number = int(number)
    if event_or_ingredient == "rest":
        initial_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_or_ingredient == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f'You earned {number} coins.')
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {event_or_ingredient}.")
        else:
            bakery_is_open = False
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {event_or_ingredient}.")


