budget = float(input())
category = input()
number_of_ppl = float(input())
ticket_price = 0

if 1 <= number_of_ppl <= 4:
    budget = budget - (budget * 0.75)
elif 5 <= number_of_ppl <= 9:
    budget = budget - (budget * 0.6)
elif 10 <= number_of_ppl <= 24:
    budget = budget - (budget * 0.5)
elif 25 <= number_of_ppl <= 49:
    budget = budget - (budget * 0.4)
else:
    budget = budget - (budget * 0.25)

if category == "VIP":
    ticket_price = 499.99 * number_of_ppl
else:
    ticket_price = 249.99 * number_of_ppl

if budget >= ticket_price:
    print(f"Yes! You have {budget - ticket_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {ticket_price - budget:.2f} leva.")




