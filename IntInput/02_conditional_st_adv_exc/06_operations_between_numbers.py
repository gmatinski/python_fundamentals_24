number1 = int(input())
number2 = int(input())
operator = input()
total = 0
even_odd = ""

if operator == "+":
    total = number1 + number2

elif operator == "-":
    total = number1 - number2

elif operator == "*":
    total = number1 * number2

elif operator == "/":
    if number2 != 0:
        total = number1 / number2
    else:
        print(f"Cannot divide {number1} by zero")

elif operator == "%":
    if number2 != 0:
        total = number1 % number2
    else:
        print(f"Cannot divide {number1} by zero")

if total % 2 == 0:
    even_odd = "even"
else:
    even_odd = "odd"

if operator == "+":
    print(f"{number1} {operator} {number2} = {number1 + number2} - {even_odd}")
elif operator == "-":
    print(f"{number1} {operator} {number2} = {number1 - number2} - {even_odd}")
elif operator == "*":
    print(f"{number1} {operator} {number2} = {number1 * number2} - {even_odd}")

if operator == "/" and number2 != 0:
    print(f"{number1} {operator} {number2} = {total:.2f}")

if operator == "%" and number2 != 0:
    print(f"{number1} {operator} {number2} = {total}")
