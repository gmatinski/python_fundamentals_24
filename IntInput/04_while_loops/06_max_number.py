import sys
max_number = -sys.maxsize
command = input()

while command != "Stop":
    current_num = int(command)
    if current_num > max_number:
        max_number = current_num
    command = input()
print(max_number)
