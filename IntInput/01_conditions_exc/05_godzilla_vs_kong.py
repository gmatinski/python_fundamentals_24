movie_budget = float(input())
number_of_statist = int(input())
price_clothing_person = float(input())
decor = movie_budget * 0.1
discount_clothing = price_clothing_person * 0.1

if number_of_statist >= 150:
    price_clothing_person -= discount_clothing

total_sum_clothing = price_clothing_person * number_of_statist

total_needed = total_sum_clothing + decor

difference = movie_budget - total_needed
if movie_budget >= total_needed:
    print("Action!", end="\n" f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!", end="\n" f"Wingard needs {abs(difference):.2f} leva more.")


