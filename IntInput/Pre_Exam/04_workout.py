import math

number_of_days = int(input())
km_run_first_day = float(input())
total_km = km_run_first_day
total_of_all = 0
for i in range(1,number_of_days +1):
    daily_percent = int(input())
    total_km += total_km * daily_percent / 100
    total_of_all += total_km
total_of_all = total_of_all + km_run_first_day
if total_of_all >= 1000:
    print(f"You've done a great job running {math.ceil(total_of_all - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - total_of_all)} more kilometers")
