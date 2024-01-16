a = float(input())
b = float(input())
h = float(input())

trapezoid = ((a + b) * h) / 2
formated_trapezoid = "{:.2f}".format(trapezoid)
print(formated_trapezoid)