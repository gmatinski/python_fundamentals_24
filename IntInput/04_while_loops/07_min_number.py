import sys
min_number = sys.maxsize
command = input()

while command != "Stop":
    current_num = int(command)
    if current_num < min_number:
        min_number = current_num
    command = input()
print(min_number)
