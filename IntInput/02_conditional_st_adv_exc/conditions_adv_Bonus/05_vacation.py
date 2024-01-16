budget = float(input())
season = input()
location = ""
accommodation = ""

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        budget = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        budget = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        budget = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        budget = budget * 0.6
else:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        budget = budget * 0.9
    else:
        location = "Morocco"
        budget = budget * 0.9

print(f"{location} - {accommodation} - {budget:.2f}")
