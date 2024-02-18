total_with_tax = 0
total = 0
tax = 0

while True:
    prices = input()
    if prices == 'special':
        break
    elif prices == 'regular':
        break

    price = float(prices)
    if price < 0:
        print("Invalid price!")
        continue

    total_with_tax += price + (price * 0.2)
    total += price
    tax += price * 0.2

if prices == 'special':
    if total > 0:
        total_with_tax -= total_with_tax * 0.1
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {total:.2f}$')
        print(f'Taxes: {tax:.2f}$')
        print("-----------")
        print(f"Total price: {total_with_tax:.2f}$")

if prices == "regular":
    if total > 0:
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {total:.2f}$')
        print(f'Taxes: {tax:.2f}$')
        print("-----------")
        print(f"Total price: {total_with_tax:.2f}$")

if total == 0:
    print("Invalid order!")
