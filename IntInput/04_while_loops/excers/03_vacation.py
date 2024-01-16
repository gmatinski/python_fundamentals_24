money_needed = float(input())
balance = float(input())
total_days = 0
spending_days = 0


while money_needed > balance:
    spend_or_save = input()
    spent_saved = float(input())
    if spend_or_save == "spend":
        balance -= spent_saved
        spending_days += 1
        total_days += 1
        if balance <= 0:
            balance = 0

    elif spend_or_save == "save":
        balance += spent_saved
        spending_days = 0
        total_days += 1
    if spending_days == 5:
        print(f"You can't save the money.\n{total_days}")
        break
    if balance >= money_needed:
        print(f"You saved the money for {total_days} days.")
        break

