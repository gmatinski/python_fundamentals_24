number = int(input())

# for i in range(1,number +1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1, number + 1):
#     print("*" * number, end="")
#     print()
#
# for i in range(1, number + 1):
#     print(" " * (number - i) + "*" * i)

for rows in range(number):
    for col in range(number):
        if rows == 0 or rows == number - 1 or col == 0 or col == number - 1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
