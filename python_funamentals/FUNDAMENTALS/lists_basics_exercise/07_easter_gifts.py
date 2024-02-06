gifts = input().split()

command = ""
while command != "No Money":
    command = input()
    command_as_list = command.split()   # make the command into a list so we can iterate example : [OutOfStock, Eggs]
    if "OutOfStock" in command:
        for index in range(len(gifts)):
            if gifts[index] == command_as_list[1]:
                gifts[index] = "None"
    elif "Required" in command:
        command_index_as_int = int(command_as_list[2])  # Required {gift} {index}" make the number to int
        if command_index_as_int in range(len(gifts)):
            gifts[command_index_as_int] = command_as_list[1]
    elif "JustInCase" in command:
        gifts[-1] = command_as_list[1]

for item in gifts:
    if item != "None":
        print(item, end=" ")
