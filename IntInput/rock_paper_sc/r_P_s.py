import random

command = input("Choose:rock,paper or scissors\n")
bot_choices = ["rock", "paper", "scissors"]
choice_bot = random.choice(bot_choices)

while True:
    if command == "rock":
        if choice_bot == "rock":
            print(f"{command} vs {choice_bot} DRAW!")
        elif choice_bot == "paper":
            print(f"{command} vs {choice_bot} LOSE!")
        elif choice_bot == "scissors":
            print(f"{command} vs {choice_bot} WIN!")
    elif command == "paper":
        if choice_bot == "rock":
            print(f"{command} vs {choice_bot} WIN!")
        elif choice_bot == "paper":
            print(f"{command} vs {choice_bot} DRAW!")
        elif choice_bot == "scissors":
            print(f"{command} vs {choice_bot} LOSE!")
    elif command == "scissors":
        if choice_bot == "rock":
            print(f"{command} vs {choice_bot} LOSE!")
        elif choice_bot == "paper":
            print(f"{command} vs {choice_bot} WIN!")
        elif choice_bot == "scissors":
            print(f"{command} vs {choice_bot} DRAW!")
    play_again = input("play,again? y/n:\n")
    if play_again == "n":
        break
    command = input("Choose again:\n")







