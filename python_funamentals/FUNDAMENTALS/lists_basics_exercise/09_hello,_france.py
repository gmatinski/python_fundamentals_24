list_of_items = input().split("|")
budget = float(input())
clothes_value = 50.00
shoes_value = 35.00
accessories_value = 20.50
price_of_items = []
increased_price_of_items = []

for item in list_of_items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if budget >= item_price:
        if item_type == "Clothes" and item_price <= clothes_value:
            budget -= item_price
            increased_price_of_item = item_price * 1.4
            price_of_items.append(item_price)
            increased_price_of_items.append(increased_price_of_item)

        elif item_type == "Shoes" and item_price <= shoes_value:
            budget -= item_price
            increased_price_of_item = item_price * 1.4
            price_of_items.append(item_price)
            increased_price_of_items.append(increased_price_of_item)

        elif item_type == "Accessories" and item_price <= accessories_value:
            budget -= item_price
            increased_price_of_item = item_price * 1.4
            price_of_items.append(item_price)
            increased_price_of_items.append(increased_price_of_item)

sum_of_original_prices = sum(price_of_items)
sum_of_new_prices = sum(increased_price_of_items)
profit = sum_of_new_prices - sum_of_original_prices
budget += sum_of_new_prices

for price in increased_price_of_items:
    print(f"{price:.2f}",end=" ")
print()
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


