def numbers(first, second, third):
    my_list.extend([first_num, second_num, third_num])
    smallest = min(my_list)
    return smallest


first_num = int(input())
second_num = int(input())
third_num = int(input())
my_list = []


print(numbers(first_num,second_num,third_num))
