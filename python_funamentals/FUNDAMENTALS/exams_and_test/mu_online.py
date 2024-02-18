initial_health = 100
bitcoins = 0
dung_rooms = input().split("|")


for index, room in enumerate(dung_rooms):
    command, number = room.split()

    if command == 'potion':
        heal_amount = min(int(number), 100 - initial_health)
        initial_health += heal_amount
        print(f'You healed for {heal_amount} hp.')
        print(f'Current health: {initial_health} hp.')
    elif command == 'chest':
        bitcoins += int(number)
        print(f'You found {int(number)} bitcoins.')
    else:
        initial_health -= int(number)
        if initial_health > 0:
            print(f'You slayed {command}.')
        elif initial_health <= 0:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {index +1}')
            break

if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")