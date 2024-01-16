projection = input()
rows = int(input())
columns = int(input())
income = 0
cinema_cap = rows * columns

if projection == "Premiere":
    income = cinema_cap * 12
elif projection == "Normal":
    income = cinema_cap * 7.50
elif projection == "Discount":
    income = cinema_cap * 5.00

print(f"{income:.2f}leva")