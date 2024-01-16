month = input()
overnight_stay = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
if month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
if month == "July" or month == "August":
    studio = 76
    apartment = 77

elif month == "May" or month == "October":
    if 7 < overnight_stay < 14:  # TUKA MOJE DA IMA PROBLEM
        studio = studio - studio * 0.05
    if overnight_stay > 14:
            studio = studio - studio * 0.3

elif month == "June" or month == "September":
    if overnight_stay > 14:
     studio = studio - studio * 0.2

if overnight_stay > 14:
    apartment = apartment - apartment * 0.1

print(f"Apartment: {overnight_stay * apartment:.2f} lv.")
print(f"Studio: {overnight_stay * studio:.2f} lv.")
