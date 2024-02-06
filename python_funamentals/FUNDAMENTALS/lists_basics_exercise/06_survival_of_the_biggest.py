numbers = [int(number) for number in input().split()]
count_of_numbers_remove = int(input())

for i in range(count_of_numbers_remove):
    lowest_number = min(numbers)
    numbers.remove(lowest_number)
list_numbers_to_string = [str(num) for num in numbers]
print(", ".join(list_numbers_to_string))

