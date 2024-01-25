number = int(input())
word = input()
my_list = []
for i in range(number):
    strings = input()
    my_list.append(strings)
print(my_list)

filtered_list = [element for element in my_list if word in element]
print(filtered_list)