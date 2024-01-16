
hours = int(input())
minutes = int(input())
min_15 = minutes + 15

if min_15 > 59:
    min_15 -= 60
    hours += 1

if hours >= 24:
    hours = 0

print(f"{hours:01d}:{min_15:02d}")
