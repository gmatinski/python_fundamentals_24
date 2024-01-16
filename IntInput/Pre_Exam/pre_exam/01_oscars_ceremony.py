hall_price = int(input())

statues_price = hall_price - hall_price * 0.3
catering = statues_price - statues_price * 0.15
sound = catering / 2

total = statues_price + catering + sound + hall_price
print(f"{total:.2f}")
