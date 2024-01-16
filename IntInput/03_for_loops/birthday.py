age = int(input())
washing_m_price = float(input())
toy_price = int(input())
toys = 0
money_gift = 0
brother_money = 0
saved_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_gift = int(i / 2) * 10
        saved_money += money_gift
        brother_money += 1
    else:
        toys += 1
total_toys_price = toys * toy_price
total_money_saved = (saved_money + total_toys_price) - brother_money
if total_money_saved >= washing_m_price:
    print(f"Yes! {total_money_saved - washing_m_price:.2f}")
else:
    print(f"No! {washing_m_price - total_money_saved:.2f}")
