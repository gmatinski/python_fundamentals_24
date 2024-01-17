# n = int(input())
# special_characters = "!@#$%^&*()-+?_=,.<>:;|`~{}[]<>'/"""
# for i in range(n):
#     string = input()
#     if any(char in string for char in special_characters):
#         print(f"{string} is not pure!")
#     else:
#         print(f"{string} is pure.")

n = int(input())

for i in range(n):
    string = input()

    if any(char in string for char in ",._"):
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")