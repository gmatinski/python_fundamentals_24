lines = int(input())
my_list = []
for i in range(lines):
    number = int(input())
    my_list.append(number)
new_list = []
command = input()
if command == "even":
    for element in my_list:
        if element % 2 == 0:
            new_list.append(element)
elif command == "odd":
    for element in my_list:
        if element % 2 != 0:
            new_list.append(element)
elif command == "negative":
    for element in my_list:
        if element < 0:
            new_list.append(element)
elif command == "positive":
    for element in my_list:
        if element >= 0:
            new_list.append(element)
print(new_list)