# 5725 min
# min=int(input("Enter time in minutes"))
# h=min//60
# m=min%60
# print("Hours=",h)
# print("Minutes=",m)
#
# print(f"{h} hours and {m} minutes more for play")
# нормата за игра на Том е 30 000  минути в година  365
# •	Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
# •	Когато почива, стопанинът му си играе с него  по 127 минути на ден.


days_off = int(input())
work_days = 365 - days_off
play_during_work = work_days * 63
play_during_off = days_off * 127
total_play = play_during_off + play_during_work
diff_from_norm = 30000 - total_play
hours = diff_from_norm // 60
minutes = diff_from_norm % 60
second_case = total_play - 30000
hours_case = second_case // 60
minutes_case = second_case % 60

if total_play < 30000:
    print("Tom sleeps well", end="\n" f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away", end="\n" f"{hours_case} hours and {minutes_case} minutes more for play")



