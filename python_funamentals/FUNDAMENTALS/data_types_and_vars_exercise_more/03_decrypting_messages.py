key = int(input())
lines = int(input())
convert_the_nums = ""
for i in range(1, lines + 1):
    characters = input()
    result_ascii = ord(characters)
    result_ascii += key
    convert_the_nums += chr(result_ascii)
print(convert_the_nums)