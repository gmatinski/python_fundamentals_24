fuel_type = input()
fuel = float(input())
club_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93
price = 0

if club_card == "Yes":
    if fuel_type == "Gasoline":
        price = (gasoline - 0.18) * fuel

    elif fuel_type == "Diesel":
        price = (diesel - 0.12) * fuel
    else:
        price = (gas - 0.08) * fuel

elif club_card == "No":
    if fuel_type == "Gasoline":
        price = gasoline * fuel
    elif fuel_type == "Diesel":
        price = diesel * fuel
    else:
        price = gas * fuel

if 20 <= fuel <= 25:
    price = price - price * 0.08

elif fuel > 25:
    price = price - price * 0.1

print(f"{price:.2f} lv.")
