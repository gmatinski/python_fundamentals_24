input_string = input()

forward_list = [int(number) for number in input_string.split()]
backwards_list = forward_list[::-1]

left_car_time = 0
right_car_time = 0
winner = ""
winner_time = 0

steps_per_car = int((len(forward_list) - 1) / 2)

for step in range(steps_per_car):
    if forward_list[step] == 0 :
        left_car_time *= 0.8
    else:
        left_car_time += forward_list[step]

    if backwards_list[step] == 0:
        right_car_time *= 0.8
    else:
        right_car_time += backwards_list[step]

if left_car_time < right_car_time:
    winner = "left"
    winner_time = left_car_time
else:
    winner = "right"
    winner_time = right_car_time

print(f"The winner is {winner} with total time: {winner_time:0.1f}")