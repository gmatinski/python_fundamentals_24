import random

random_number = random.randrange(1, 100)

while True:
    player_number = int(input("choose a number - between [1,100]\nEnter number here:"))
    if player_number > 100:
        print("Number is too high choose a number between 1 and 100")
        continue
    if player_number == random_number:
        print("You, guessed the number!")
        break
    elif player_number < random_number:
        print("The number is greater than the number you choose")
    else:
        print("The number is smaller than the number you choose")
