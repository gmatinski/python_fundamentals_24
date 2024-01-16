season = input()
km_per_month = float(input())
salary = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.75) * 4
    elif season == "Summer":
        salary = (km_per_month * 0.90) * 4
    else:
        salary = (km_per_month * 1.05) * 4
if 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.95) * 4
    elif season == "Summer":
        salary = (km_per_month * 1.10) * 4
    else:
        salary = (km_per_month * 1.25) * 4
if 10000 < km_per_month <= 20000:
    salary = (km_per_month * 1.45) * 4

salary_after_tax = salary - salary * 0.1

print(f"{salary_after_tax:.2f}")
