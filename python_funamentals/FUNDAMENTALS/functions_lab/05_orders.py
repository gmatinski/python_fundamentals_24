def calculate(order_price, quantity_pro):
    total_price = order_price * quantity_pro
    return total_price


product = input()
quantity = int(input())
price = 0
if product == "coffee":
    price = 1.50
elif product == "water":
    price = 1.00
elif product == "coke":
    price = 1.40
elif product == "snacks":
    price = 2.00

print(f"{calculate(price,quantity):.2f}")