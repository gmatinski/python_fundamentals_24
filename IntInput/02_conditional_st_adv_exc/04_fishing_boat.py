budget = int(input())
season = input()
fisherman = int(input())
rent = 0

if season == "Spring":
    rent = 3000
if season == "Summer" or season == "Autumn":
    rent = 4200
if season == "Winter":
    rent = 2600

if fisherman <= 6:
    rent = rent - rent * 0.1
elif 7 <= fisherman <= 11:
    rent = rent - rent * 0.15
elif fisherman >= 12:
    rent = rent - rent * 0.25

if fisherman % 2 == 0 and season != "Autumn":
    rent = rent - (rent * 0.05)

if budget >= rent:
    print(f"Yes! You have {budget - rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {rent - budget:.2f} leva.")
