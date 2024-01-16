start = int(input())
end = int(input())
magic_num = int(input())
combination = 0
combination_is_found = False

for first_number in range(start, end +1):
    for second_num in range(start,end+1):
        combination +=1
        result = first_number + second_num
        if result == magic_num:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combination} ({first_number} + {second_num} = {magic_num})")
else:
    print(f"{combination} combinations - neither equals {magic_num}")








