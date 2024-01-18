number = int(input())

for i in range(1, number + 1):
    sum_of_digits = 0
    check_if_special = False
    for digit in str(i):
        sum_of_digits += int(digit)
    if sum_of_digits in [5, 7, 11]:
        check_if_special = True
    print(f"{i} -> {check_if_special}")
