number_of_orders = int(input())
price = 0
total = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 > price_per_capsule or price_per_capsule> 100:
        continue
    elif 1 > days or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * capsules_per_day
    print(f"The price for the coffee is: ${price:.2f}")
    total += price
print(f"Total: ${total:.2f}")
