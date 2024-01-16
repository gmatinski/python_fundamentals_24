price_per_kg_Veg = float(input())
price_per_kg_Fru = float(input())
total_kg_veg = int(input())
total_kg_fru = int(input())

veggies = price_per_kg_Veg * total_kg_veg
fruits = price_per_kg_Fru * total_kg_fru

total = (veggies + fruits) / 1.94 #price from lev to eur
format_total = "{:.2f}".format(total)
print(format_total)