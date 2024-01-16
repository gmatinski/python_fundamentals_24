sum_expected = int(input())
counter = 1
total = 0
sum_in_cash = 0
sum_with_card = 0
counter_cash = 0
counter_card = 0

while total < sum_expected:
    prices_of_stuff = input()
    if prices_of_stuff.isdigit():
        prices_of_stuff = int(prices_of_stuff)
        if counter % 2 == 1:   # if it is payed in cash
            counter += 1
            if prices_of_stuff > 100:
                print("Error in transaction!")
            else:
                print("Product sold!")
                counter_cash += 1
                sum_in_cash += prices_of_stuff
                total += prices_of_stuff
        elif counter % 2 == 0:
            counter += 1
            if prices_of_stuff < 10:
                print("Error in transaction!")
            else:
                print("Product sold!")
                counter_card += 1
                sum_with_card += prices_of_stuff
                total += prices_of_stuff
    if total >= sum_expected:
        print(f"Average CS: {sum_in_cash / counter_cash:.2f}")
        print(f"Average CC: {sum_with_card / counter_card:.2f}")
        break
    if prices_of_stuff == "End":
        if total < sum_expected:
            print(f"Failed to collect required money for charity.")
            break



