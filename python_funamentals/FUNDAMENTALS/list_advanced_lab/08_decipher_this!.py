input_text = list(map(str, input().split(' ')))

def digist_to_letter(word):
    char_list = list(word)
    num_list = []

    while True:
        if char_list[0].isdigit():
            num_list.append(char_list[0])
            char_list.pop(0)
        else:
            break

    num_list = ''.join(num_list)
    missing_letter = list(chr(int(num_list)))
    char_list = missing_letter + char_list

    return ''.join(char_list)

def swap_letters(word):
    char_list = list(word)
    char_list[1], char_list[-1] = char_list[-1], char_list[1]
    return ''.join(char_list)

for i in range(len(input_text)):
    input_text[i] = digist_to_letter(input_text[i])
    input_text[i] = swap_letters(input_text[i])

output_string = ' '.join(input_text)
print(output_string)