n = int(input())
current_num = 1
check = False
for row in range(1, n+1):
    for col in range(1,row + 1):
        if current_num > n:
            check = True
            break
        print(current_num, end="")
        current_num += 1
    if check:
        break
    print()




