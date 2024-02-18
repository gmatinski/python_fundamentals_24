array_list = [int(num) for num in input().split()]

while True:
    line = input()
    if line == 'end':
        break

    command, *args = line.split()
    if command == 'swap':
        first_arg, second_arg = map(int, args)
        array_list[first_arg], array_list[second_arg] = array_list[second_arg], array_list[first_arg]
    elif command == 'multiply':
        first_arg, second_arg = map(int, args)
        array_list[first_arg] = array_list[first_arg] * array_list[second_arg]
    elif command == 'decrease':
        for i in range(len(array_list)):
            array_list[i] -= 1
array_list_str = [str(item) for item in array_list]
print(', '.join(array_list_str))