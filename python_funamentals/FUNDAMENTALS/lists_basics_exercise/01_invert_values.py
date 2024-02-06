numbers = input()    # 1 2 -3 -3 5
my_list = numbers.split(" ")
for i in range(len(my_list)):
    my_list[i] = -int(my_list[i])
print(my_list)

