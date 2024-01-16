a = float(input())
if a >= 26 and a <= 35:
    print("Hot")
elif a >= 20.1 and a <= 25.9:
    print("Warm")
elif a >= 15.00 and a <= 20.00:
    print("Mild")
elif a >= 12.00 and a <= 14.9:
    print("Cool")
elif 5.00 <= a <= 11.9:
    print("Cold")
else:
    print("unknown")

