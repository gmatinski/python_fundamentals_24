import math

days_away = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000  # to kg

food_needed = days_away * (dog_food + cat_food + turtle_food)

if food >= food_needed:
    print(f"{math.floor(food - food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(food_needed - food)} more kilos of food are needed.")
