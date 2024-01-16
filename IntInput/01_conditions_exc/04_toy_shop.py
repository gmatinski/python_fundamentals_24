price_of_trip = float(input())
num_of_puzzles = int(input())
num_of_dolls = int(input())
num_of_bears = int(input())
num_of_minions = int(input())
num_of_trucks = int(input())
shop_rent = 0
total_price_w_disc = 0

total_toys = num_of_puzzles + num_of_dolls + num_of_bears + num_of_minions + num_of_trucks
total_price = num_of_puzzles * 2.60 \
              + num_of_dolls * 3 \
              + num_of_bears * 4.10 \
              + num_of_minions * 8.20 \
              + num_of_trucks * 2
if total_toys >= 50:
    total_price_w_disc = total_price * 0.25
    total_price = total_price - total_price_w_disc

shop_rent = total_price * 0.1

total_price = total_price - shop_rent

if total_price >= price_of_trip:
    print(f"Yes! {total_price - price_of_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_of_trip - total_price:.2f} lv needed.")
