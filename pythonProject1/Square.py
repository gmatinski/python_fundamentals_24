number = int(input())

for stars in range(number):
    if stars < 1 or stars == number - 1:
        print("*" * number)
    else:
        print("*" + " " * (number - 2) + "*")




