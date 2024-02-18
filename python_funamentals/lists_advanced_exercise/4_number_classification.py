def positives_nums(list_numbers):
    return ', '.join([num for num in numbers_list if int(num) >= 0])


def negative_nums(list_nums):
    return ', '.join([num for num in numbers_list if int(num) < 0 ])


def even_nums(list_nums):
    return ', '.join([num for num in numbers_list if int(num) % 2 == 0])


def odd(list_nums):
    return ', '.join([num for num in numbers_list if int(num) % 2 !=0])


numbers_list = input().split(', ')
print(f"Positive: {positives_nums(numbers_list)}")
print(f"Negative: {negative_nums(numbers_list)}")
print(f"Even: {even_nums(numbers_list)}")
print(f"Odd: {odd(numbers_list)}")