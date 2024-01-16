destination = input()

while destination != "End":
    money_needed = float(input())
    her_money = 0
    while her_money < money_needed:
        saved_money = float(input())
        her_money += saved_money
    print(f"Going to {destination}!")
    destination = input()



