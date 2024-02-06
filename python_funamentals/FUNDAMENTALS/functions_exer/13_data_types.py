def data_type(choice):
    if choice == "int":
        return int(number) * 2
    elif choice == "real":
        return f"{float(number) * 1.5:.2f}"
    elif choice == "string":
        return f'${number}$'


input_line = input()
number = input()
print(data_type(input_line))