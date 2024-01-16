time_first = int(input())
time_second = int(input())
time_third = int(input())

total = time_first + time_second + time_third

minutes = total // 60
seconds = total % 60

print(f"{minutes}:{seconds :02d}")
