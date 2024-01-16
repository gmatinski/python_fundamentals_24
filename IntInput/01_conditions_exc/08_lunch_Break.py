import math

series = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
rest_time = break_length / 4
break_left = break_length - (lunch_time + rest_time)

if break_left >= episode_length:
    print(
        f"You have enough time to watch {series} and left with {math.ceil(break_left - episode_length )} minutes free time.")
else:
    print(
        f"You don't have enough time to watch {series}, you need {math.ceil(episode_length - break_left)} more minutes.")
