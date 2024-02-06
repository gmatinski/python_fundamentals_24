string = input().split(", ")
new_list = []
zero = []
for numbers in string:
    number = int(numbers)
    if number != 0:
        new_list.append(number)
    else:
        zero.append(number)
new_list.extend(zero)
print(new_list)

# string = input().split(", ")
# for numbers in string:
#     if numbers == "0":
#         string.remove(numbers)


