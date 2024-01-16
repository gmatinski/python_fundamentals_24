import sys
numbers = int(input()) # == 2
max_num = -sys.maxsize
sum_numbers = 0

for i in range(numbers): # == 2
    num = int(input())   # (2) --> 3, ---> 3
    if num > max_num:
        max_num = num    # max_num == 3,
    sum_numbers += num    # 3 + 3 = 6
if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    sum_numbers = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_numbers)}")

