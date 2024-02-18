initial_energy = int(input())
battles_won = 0
distance_command = input()
while distance_command != 'End of battle':
    distance_to_enemy = int(distance_command)
    if initial_energy - distance_to_enemy < 0:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy')
        break
    initial_energy -= distance_to_enemy
    if initial_energy >= 0:
        battles_won += 1
    if battles_won % 3 == 0:
        initial_energy += battles_won
    distance_command = input()
if distance_command == 'End of battle':
    print(f'Won battles: {battles_won}. Energy left: {initial_energy}')

    m