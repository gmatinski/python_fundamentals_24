command = input()
coffee = 0  # lowercase = 1 // uppercase = 2

while command != "END":
    if command.lower() not in ("coding","dog","cat","movie"):
        command = input()
        continue
    else:
        if command.isupper():
            coffee += 2
        elif command.islower():
            coffee += 1
    command = input()
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
