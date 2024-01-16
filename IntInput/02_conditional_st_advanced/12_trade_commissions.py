town = input()
sells = float(input())
percent = 0

if town == "Sofia":
    if 0 <= sells <= 500:
        percent = 0.05
    elif 500 <= sells <= 1000:
        percent = 0.07
    elif 1000 <= sells <= 10000:
        percent = 0.08
    elif sells > 10000:
        percent = 0.12
if town == "Varna":
    if 0 <= sells <= 500:
        percent = 0.045
    elif 500 <= sells <= 1000:
        percent = 0.075
    elif 1000 <= sells <= 10000:
        percent = 0.1
    elif sells > 10000:
        percent = 0.13
if town == "Plovdiv":
    if 0 <= sells <= 500:
        percent = 0.055
    elif  500 <= sells <= 1000:
        percent = 0.08
    elif 1000 <= sells <= 10000:
        percent = 0.12
    elif sells > 10000:
        percent = 0.145
if percent == 0:
    print("error")
else:
    print(f"{sells * percent:.2f}")
