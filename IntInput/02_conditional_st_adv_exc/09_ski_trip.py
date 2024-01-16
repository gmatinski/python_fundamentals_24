days = int(input())
type_room = input()
review = input()

nights = days - 1
price = 0

if type_room == "room for one person":
    price = nights * 18

if type_room == "apartment":
    if days < 10:
        price = nights * 25 - (nights * 25) * 0.3
    elif 10 <= days <= 15:
        price = nights * 25 - (nights * 25) * 0.35
    else:
        price = nights * 25 - (nights * 25) * 0.5

if type_room == "president apartment":
    if days < 10:
        price = nights * 35 - (nights * 35) * 0.1
    elif 10 <= days <= 15:
        price = nights * 35 - (nights * 35) * 0.15
    else:
        price = nights * 35 - (nights * 35) * 0.2

if review == "positive":
    price = price + price * 0.25
else:
    price = price - price * 0.1

print(f"{price:.2f}")
