# number = int(input())
# text = ""
# if number > 1:
#     for i in range(2, number + 1):
#         if i % 2 == 0:
#             text = "False"
#         else:
#             text = "True"
#
# print(text)

number = int(input())
text = "True"  # Assume the number is prime initially

if number > 1:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            text = "False"
            break  # Exit the loop if a divisor is found

print(text)
