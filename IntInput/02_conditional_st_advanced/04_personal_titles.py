age = float(input())
sex = input()

if age >= 16 and (sex == "f" or sex == "m") :
    if sex == "m":
        print("Mr.")
    elif sex == "f":
        print("Ms.")
if age < 16 and (sex == "f" or sex == "m") :
    if sex == "m":
        print("Master")
    elif sex == "f":
        print("Miss")
