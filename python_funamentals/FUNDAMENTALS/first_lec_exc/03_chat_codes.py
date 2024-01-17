col = int(input())

for n in range(col):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number not in (88,86) and number < 88:
        print("GREAT!")
    else:
        print("Bye.")




