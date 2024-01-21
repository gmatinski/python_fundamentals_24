lines = int(input())
check = ""
for line in range(1,lines +1):
    input_line = input()
    if input_line == "(" or input_line == ")":
        check += input_line
        if check == "(":
            continue
        elif check == "()":
            check = ""
if check == "":
    print("BALANCED")
else:
    print("UNBALANCED")
