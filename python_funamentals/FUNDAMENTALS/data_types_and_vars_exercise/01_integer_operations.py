integers = 4
first_number = 0
second_number = 0
third_number = 0
fourth_number = 0
for current_num in range(1,integers + 1):
    number = int(input())
    if current_num == 1:
        first_number = number
    elif current_num == 2:
        second_number = number
    elif current_num == 3:
        third_number = number
    elif current_num == 4:
        fourth_number = number
final_number = int((first_number + second_number) / third_number) * fourth_number
print(final_number)


