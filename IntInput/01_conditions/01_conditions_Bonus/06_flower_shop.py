import math

number_magnolia = int(input())
number_z = int(input())
number_rose = int(input())
number_cactus = int(input())
present_price = float(input())

total = number_magnolia * 3.25 + number_z * 4 + number_rose * 3.50 + number_cactus * 8

percent = total * 0.05
after_tax = total - percent

if after_tax >= present_price:
    print(f"She is left with {math.floor(after_tax - present_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(present_price - after_tax)} leva.")
