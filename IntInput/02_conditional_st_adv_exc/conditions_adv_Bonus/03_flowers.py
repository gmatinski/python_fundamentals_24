hriz = int(input())
rose = int(input())
lale = int(input())
season = input()
holiday = input()
price_hz = 0
price_rs = 0
price_l = 0
total_flowers = hriz + rose + lale
price_total = 0

if season == "Spring" or season == "Summer":
    price_hz = 2.00 * hriz
    price_rs = 4.10 * rose
    price_l = 2.50 * lale
    price_total = price_hz + price_rs + price_l
elif season == "Autumn" or season == "Winter":
    price_hz = 3.75 * hriz
    price_rs = 4.50 * rose
    price_l = 4.15 * lale
    price_total = price_hz + price_rs + price_l

if holiday == "Y":
    price_total += price_total * 0.15
if lale > 7 and season == "Spring":
    price_total -= price_total * 0.05
elif rose >= 10 and season == "Winter":
    price_total -= price_total * 0.1
if total_flowers > 20:
    price_total -= price_total * 0.2
print(f"{price_total + 2:.2f}")
