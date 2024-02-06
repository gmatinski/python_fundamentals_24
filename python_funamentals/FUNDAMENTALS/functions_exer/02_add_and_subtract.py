def sum_numbers(some_nums: list):
    return sum(some_nums)


def subtract(result, third):
    return result - third


# def add_and_subtract(first,second,third):
#     return sum_numbers(),subtract()


first_num = int(input())
second_num = int(input())
third_num = int(input())

first_nums_sum = sum_numbers([first_num, second_num])
print(subtract(first_nums_sum,third_num))

