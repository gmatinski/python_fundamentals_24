def minimum(min_num):
    return min(numbers_as_digits)


def maximum(max_num):
    return max(numbers_as_digits)


def summed(sum_num):
    return sum(numbers_as_digits)


numbers_as_string = input().split()
numbers_as_digits = [int(number) for number in numbers_as_string]

print(f"The minimum number is {minimum(numbers_as_digits)}")
print(f"The maximum number is {maximum(numbers_as_digits)}")
print(f"The sum number is: {summed(numbers_as_digits)}")