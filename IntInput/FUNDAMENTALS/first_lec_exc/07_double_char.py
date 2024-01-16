command = input()

while command != "End":
    for char in command:
        if command == "SoftUni":
            break
        else:
            print(char * 2, end="")
    command = input()
    print()
