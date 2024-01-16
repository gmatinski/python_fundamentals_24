first_num = int(input())
second_num = int(input())
for i in range(first_num, second_num +1):
    current_num_str = str(i)
    # 10_00_00
    even_sum = 0
    odd_sum = 0
    for j in range(0, len(current_num_str)):
        digit = current_num_str[j]
        if j % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(i, end=" ")