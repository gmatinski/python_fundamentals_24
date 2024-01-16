first_number = int(input())
second_number = int(input())
third_number = int(input())
list_with_prime_nums = [2, 3, 5, 7]

for i in range(2, first_number + 1, 2):
    for j in list_with_prime_nums:
        if j <= second_number:
            for k in range(2, third_number + 1, 2):
                print(f"{i} {j} {k}")
