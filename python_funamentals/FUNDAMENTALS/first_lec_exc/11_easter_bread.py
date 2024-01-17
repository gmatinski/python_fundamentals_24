budget = float(input())
flour_one_kg_price = float(input())
pack_of_eggs_price = flour_one_kg_price * 0.75  # 75%
price_milk = (flour_one_kg_price * 0.25) + flour_one_kg_price  # 1.56
loaf = 0
colored_eggs = 0
price_of_one_loaf = pack_of_eggs_price + flour_one_kg_price + (price_milk * 0.250)

while budget >= price_of_one_loaf:
    budget -= price_of_one_loaf
    loaf += 1
    colored_eggs += 3

    if loaf % 3 == 0:
        colored_eggs -= loaf - 2

print(f"You made {loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

