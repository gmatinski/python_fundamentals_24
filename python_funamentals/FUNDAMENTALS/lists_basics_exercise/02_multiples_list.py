factor = int(input())
count = int(input())

my_list = list(range(1, count + 1))
for i in range(len(my_list)):
    my_list[i] *= factor
print(my_list)
