money_input = input()
total = 0
while money_input != "NoMoreMoney":
    current_sum = float(money_input)
    if current_sum < 0:
        print("Invalid operation!")
        break
    money_input = input()
    total += current_sum
    print(f"Increase: {current_sum:.2f}")
print(f"Total: {total:.2f}")

