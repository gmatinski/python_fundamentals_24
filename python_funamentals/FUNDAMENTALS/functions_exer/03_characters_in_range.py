def chars(first, second):
    all_the_chars = []
    for current_char in range(ord(first)+1,ord(second)):
        all_the_chars.append(chr(current_char))
    return all_the_chars


first_char = input()
second_char = input()
final_result = chars(first_char,second_char)
print(" ".join(final_result))
