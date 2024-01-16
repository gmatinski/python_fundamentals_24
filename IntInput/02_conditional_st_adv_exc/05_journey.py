budget = float(input())
season = input()
destination = ""
camp_hotel = ""

if season == "summer":
    camp_hotel = "Camp"
elif season == "winter":
    camp_hotel = "Hotel"


if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget = budget * 0.3
    elif season == "winter":
        budget =  budget * 0.7


if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget =  budget * 0.4
    elif season == "winter":
        budget =  budget * 0.8

elif budget > 1000:
    destination = "Europe"
    budget =  budget * 0.9
    if destination == "Europe":
        camp_hotel = "Hotel"

print(f"Somewhere in {destination}")
print(f"{camp_hotel} - {budget:.2f}")

