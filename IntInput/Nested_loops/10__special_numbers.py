n = int(input())
str_num = ""
counter = 0
for i in range(1111,9999+1):
    character = str(i)
    for j in range(0, len(character)):
        num = character[j]
        if int(num) != 0 and n % int(num) == 0:
            str_num += num
            counter += 1
    if counter > 3:
        print(str_num, end=" ")
    counter = 0
    str_num = ""

# typ i truden varqnt po lesen e s 4 for loops ot 1,10 i print(f"chetirte for loops") prowerka dali se delqt i
# spestqwam 1 chas










