stage_of_championship = input()  # Quarter final, Semi final Final
type_of_ticket = input()  # Standard, Premium, VIP
number_of_tickets = int(input())  # [1...30]
pic_with_trophie = input()  # Y/N
ticket_price = 0
total_for_pic = 0

if type_of_ticket == "Standard":
    if stage_of_championship == "Quarter final":
        ticket_price = 55.50
    elif stage_of_championship == "Semi final":
        ticket_price = 75.88
    elif stage_of_championship == "Final":
        ticket_price = 110.10
elif type_of_ticket == "Premium":
    if stage_of_championship == "Quarter final":
        ticket_price = 105.20
    elif stage_of_championship == "Semi final":
        ticket_price = 125.22
    elif stage_of_championship == "Final":
        ticket_price = 160.66
else:
    if stage_of_championship == "Quarter final":
        ticket_price = 118.90
    elif stage_of_championship == "Semi final":
        ticket_price = 300.40
    elif stage_of_championship == "Final":
        ticket_price = 400

total_price = number_of_tickets * ticket_price
if pic_with_trophie == "Y" and total_price <= 4000:
    total_for_pic = number_of_tickets * 40
if total_price > 4000:
    total_price -= total_price * 0.25
elif 2500 < total_price <= 4000:
    total_price -= total_price * 0.1

total_price += total_for_pic
print(f"{total_price:.2f}")
