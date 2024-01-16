numbers = int(input())
left_sum = 0
right_sum = 0

for i in range(numbers * 2):
    current_number = int(input())
    if i < numbers:
        left_sum += current_number
    else:
        right_sum += current_number
if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(right_sum - left_sum)}")
