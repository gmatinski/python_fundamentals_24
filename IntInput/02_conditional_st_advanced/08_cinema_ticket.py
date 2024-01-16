day = input()

if day in ("Monday", "Tuesday", "Friday"):
    print(12)
elif day == "Wednesday" or day == "Thursday":
    print(14)
else:
    print(16)