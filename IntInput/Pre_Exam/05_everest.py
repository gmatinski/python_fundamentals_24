text = input()
meters = int(input())
day = 1
daily_m = 5364
while text != "END":
    if text == "Yes":
        day += 1
        if day > 5:
            print(f"Failed!\n{daily_m}")
            break
    daily_m += meters
    if daily_m >= 8848:
        print(f"Goal reached for {day} days!")
        break
    text = input()
    if text == "END" and daily_m >= 8848:
        print(f"Goal reached for {day} days!")
        break
    elif text == "END" and daily_m < 8848:
        print(f"Failed!\n{daily_m}")
        break
    meters = int(input())
