lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0
shield_counter = 0
for fights in range(1, lost_fights + 1):
    if fights % 2 == 0:
        total_price += helmet_price
        if fights % 3 == 0:
            total_price += shield_price
            shield_counter += 1
    if fights % 3 == 0:
        total_price += sword_price
    if shield_counter > 1 and shield_counter % 2 == 0:
        total_price += armor_price
        shield_counter = 0
print(f"Gladiator expenses: {total_price:.2f} aureus")
