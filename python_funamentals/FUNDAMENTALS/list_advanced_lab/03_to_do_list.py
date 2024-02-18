notes = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    token = command.split("-")
    importance = int(token[0]) -1
    note = token[1]
    notes.pop(importance)
    notes.insert(importance,note)
result = [element for element in notes if element !=0]
print(result)