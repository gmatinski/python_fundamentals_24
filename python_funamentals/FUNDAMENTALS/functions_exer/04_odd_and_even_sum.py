def sum_even_odd(number):
    sum_even = 0
    sum_odd = 0
    for digit in number:
        int_digit = int(digit)
        if int_digit % 2 == 0:  # if num is even
            sum_even += int_digit
        elif int_digit % 2 != 0:
            sum_odd += int_digit
    return sum_even, sum_odd


number_as_string = input()
result = sum_even_odd(number_as_string)
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")