budget = float(input())
season = input()
class_car = ""
type_vehicle = ""

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_vehicle = "Cabrio"
        budget = budget * 0.35
    elif season == "Winter":
        type_vehicle = "Jeep"
        budget = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_vehicle = "Cabrio"
        budget = budget * 0.45
    elif season == "Winter":
        type_vehicle = "Jeep"
        budget = budget * 0.8
else:
    class_car = "Luxury class"
    type_vehicle = "Jeep"
    budget = budget * 0.9

print(f"{class_car}")
print(f"{type_vehicle} - {budget:.2f}")
