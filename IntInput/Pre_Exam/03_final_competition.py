number_of_dancers = int(input())
points = float(input())
season = input()
place = input()
total_points = 0

if place == "Bulgaria":
    total_points = points * number_of_dancers
elif place == "Abroad":
    total_points = points * number_of_dancers
    total_points += total_points * 0.5

if place == "Bulgaria" and season == "summer":
    total_points -= total_points * 0.05
elif place == "Bulgaria" and season == "winter":
    total_points -= total_points * 0.08
elif place == "Abroad" and season == "summer":
    total_points -= total_points * 0.1
elif place == "Abroad" and season == "winter":
    total_points -= total_points * 0.15

money_for_charity = total_points * 0.75
price_for_dancers = (total_points - money_for_charity) / number_of_dancers
print(f"Charity - {money_for_charity:.2f}\nMoney per dancer - {price_for_dancers:.2f}")


