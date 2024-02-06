input_string = input()  # receiving the sequence of numbers
list_of_numbers = [number for number in input_string.split()]  # converting the numbers to a integers in a list
some_text = input()


for number in list_of_numbers:
    # Convert the integer to a list of its digits
    digits = [int(digit) for digit in number]
    current_seq_sum = sum(digits)
    if current_seq_sum >= len(some_text):
        char_to_print = (some_text[current_seq_sum % len(some_text)])
        some_text = some_text.replace(some_text[current_seq_sum % len(some_text)], '', 1)

    else:
        char_to_print = (some_text[current_seq_sum])
        some_text = some_text.replace(some_text[current_seq_sum], '', 1)

    print(char_to_print, end="")
