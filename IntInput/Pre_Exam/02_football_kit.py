t_shirt_price = float(input())
price_of_ball = float(input())

price_of_shorts = t_shirt_price * 0.75
price_of_socks = price_of_shorts * 0.2
shoes_price = 2*(t_shirt_price + price_of_shorts)

total_price = t_shirt_price + price_of_shorts + price_of_socks + shoes_price
total_price -= total_price * 0.15

if total_price >= price_of_ball:
    print(f"Yes, he will earn the world-cup replica ball!\nHis sum is {total_price:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.\nHe needs {price_of_ball - total_price:.2f} lv. more.")