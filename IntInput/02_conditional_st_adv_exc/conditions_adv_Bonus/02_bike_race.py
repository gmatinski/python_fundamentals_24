juniors = int(input())
seniors = int(input())
type_track = input()
tax_juniors = 0
tax_seniors = 0
total_tax = 0

if type_track == "trail":
    tax_juniors = juniors * 5.50
    tax_seniors = seniors * 7
    total_tax = tax_seniors + tax_juniors
elif type_track == "cross-country":
    tax_juniors = juniors * 8
    tax_seniors = seniors * 9.50
    total_tax = tax_seniors + tax_juniors
    if juniors + seniors >= 50:
        total_tax = (tax_juniors + tax_seniors) - (tax_juniors + tax_seniors) * 0.25
elif type_track == "downhill":
    tax_juniors = juniors * 12.25
    tax_seniors = seniors * 13.75
    total_tax = tax_seniors + tax_juniors
elif type_track == "road":
    tax_juniors = juniors * 20
    tax_seniors = seniors * 21.50
    total_tax = tax_seniors + tax_juniors

total_tax -= total_tax * 0.05

print(f"{total_tax:.2f}")
