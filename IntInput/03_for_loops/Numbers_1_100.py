sum_of_num = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range (sum_of_num ):
    numbers = int(input())
    if numbers < 200:
        p1 = p1 + 1
    elif 200 <= numbers <= 399:
        p2 = p2 + 1
    elif 400 <= numbers <= 599:
        p3 = p3 + 1
    elif 600 <= numbers <=799:
        p4 = p4 + 1
    else:
        p5 = p5 + 1
p1_percent = p1 / sum_of_num * 100
p2_percent = p2 / sum_of_num * 100
p3_percent = p3 / sum_of_num * 100
p4_percent = p4 / sum_of_num * 100
p5_percent = p5 / sum_of_num * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")




