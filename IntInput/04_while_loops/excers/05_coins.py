change = float(input())
change_to_cents = int(change * 100)         # 1,2,5,10,20,50,100,200
count = 0
# 222 200 20 2
while change_to_cents > 0:
    if change_to_cents >= 200:
        change_to_cents -= 200
        count += 1
    elif change_to_cents >= 100:
        change_to_cents -= 100
        count += 1
    elif change_to_cents >= 50:
        change_to_cents -= 50
        count += 1
    elif change_to_cents >= 20:
        change_to_cents -= 20
        count += 1
    elif change_to_cents >= 10:
        change_to_cents -= 10
        count += 1
    elif change_to_cents >= 5:
        change_to_cents -= 5
        count += 1
    elif change_to_cents >= 2:
        change_to_cents -= 2
        count += 1
    elif change_to_cents >= 1:
        change_to_cents -= 1
        count += 1

print(count)








