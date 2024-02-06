def factorial_first(number_one):
    result = 1
    for i in range(1, number_one + 1):
        result *= i
    return result


def second_factorial(number_two):
    result = 1
    for j in range(1, number_two + 1):
        result *=j
    return result


first_num = int(input())
second_num = int(input())

print(f"{factorial_first(first_num)/ second_factorial(second_num):.2f}")