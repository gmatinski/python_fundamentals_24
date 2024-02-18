def reduce_values(target_list,index):
    special_value = target_list[index]
    target_list[index] = -1
    for i in range(len(target_list)):
        if target_list[i] == -1:
            continue
        if special_value < target_list[i]:
            target_list[i] -= special_value
        else:
            target_list[i] += special_value
    return target_list


target_values = [int(num) for num in input().split()]

command = input()
count_of_shot_targets = 0
while command != 'End':
    idx = int(command)
    if 0 <= idx < len(target_values) and target_values[idx] != -1:
        reduce_values(target_values,idx)
        count_of_shot_targets +=1
    command = input()

convert_target_values_to_str = [str(num) for num in target_values]
print(f"Shot targets: {count_of_shot_targets} -> {' '.join(convert_target_values_to_str)}")


