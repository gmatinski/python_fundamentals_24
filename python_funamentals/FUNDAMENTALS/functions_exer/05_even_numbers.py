number_as_string = input().split()
number_as_int = [int(number) for number in number_as_string]

even_nums = lambda num: num % 2 == 0
result = list(filter(even_nums,number_as_int))

print(result)