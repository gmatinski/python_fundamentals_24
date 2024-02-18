numbers = input().split(", ")
new_list = []

for index, num in enumerate(numbers):
    if int(num) % 2 == 0:
        new_list.append(index)
print(new_list)
