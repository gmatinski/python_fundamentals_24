# •	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# •	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# •	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# •	4ти ред: брой работници – цяло число в интервала [1 … 20]
import math

field_in_sq_meters = int(input())
grape_for_one_sq = float(input())
needed_wine_liters = int(input())
num_of_workers = int(input())

total_grape = grape_for_one_sq * field_in_sq_meters
wine = total_grape * 0.4
liters = wine / 2.5
if_left = liters - needed_wine_liters

if liters >= needed_wine_liters:
    print(f"Good harvest this year! Total wine: {math.floor(liters)} liters.", end="\n"
     f"{math.ceil(if_left)} liters left -> {math.ceil(if_left / num_of_workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(needed_wine_liters - liters)} liters wine needed.")
