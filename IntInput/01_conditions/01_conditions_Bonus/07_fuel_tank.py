fuel = input()
liters = float(input())

if fuel in ("Diesel", "Gasoline", "Gas") and liters >= 25:
    print(f"You have enough {fuel.lower()}.")
elif fuel in ("Diesel", "Gasoline", "Gas") and liters < 25:
    print(f"Fill your tank with {fuel.lower()}!")
elif fuel != ("Diesel", "Gasoline", "Gas"):
    print("Invalid fuel!")
