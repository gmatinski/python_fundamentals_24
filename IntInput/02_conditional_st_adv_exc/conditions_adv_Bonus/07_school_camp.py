season = input()
group = input()
number_of_students = int(input())
number_of_nights = int(input())
price = 0
sport = ""

if group == "boys" or group == "girls":
    if season == "Winter":
        price = 9.60 * number_of_nights * number_of_students
    elif season == "Spring":
        price = 7.20 * number_of_nights * number_of_students
    else:
        price = 15 * number_of_nights * number_of_students
if group == "mixed":
    if season == "Winter":
        price = 10 * number_of_nights * number_of_students
    elif season == "Spring":
        price = 9.50 * number_of_nights * number_of_students
    else:
        price = 20 * number_of_nights * number_of_students

if number_of_students >= 50:
    price -= price * 0.5
elif 20 <= number_of_students < 50:
    price -= price * 0.15
elif 10 <= number_of_students < 20:
    price -= price * 0.05

if group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    else:
        sport = "Volleyball"
if group == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    else:
        sport = "Football"
if group == "mixed":
    if season == "Winter":
        sport = "ski"
    elif season == "Spring":
        sport = "Cycling"
    else:
        sport = "Swimming"
print(f"{sport} {price:.2f} lv.")