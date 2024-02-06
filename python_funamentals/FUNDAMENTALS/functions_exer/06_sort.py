numbers_as_string = input().split()
numbers_as_digits = [int(number) for number in numbers_as_string]

print(sorted(numbers_as_digits))