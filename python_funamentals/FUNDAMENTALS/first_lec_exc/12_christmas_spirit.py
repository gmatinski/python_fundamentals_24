quantity_of_decoration = int(input())
day_until_xmas = int(input())
ornament_price = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
spirit = 0
price = 0
for day in range(1,day_until_xmas+1):
    if day % 11 == 0:
        quantity_of_decoration += 2
    if day % 2 == 0:
        price += ornament_price * quantity_of_decoration   # ornaments
        spirit += 5
    if day % 3 == 0:
        price += (tree_skirt + tree_garland) * quantity_of_decoration   # tree skirts and tree garlands
        spirit += 3 + 10
    if day % 5 == 0:
        price += tree_lights * quantity_of_decoration  # tree lights
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        price += tree_garland + tree_lights + tree_skirt

if day_until_xmas % 10 == 0:
    spirit -= 30
print(f"Total cost: {price}\nTotal spirit: {spirit}")






