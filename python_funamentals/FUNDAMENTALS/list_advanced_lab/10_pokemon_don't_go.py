import re

input_string = input()

# Use regular expression to split the string based on # or @
words = re.split(r'[#@]', input_string)

# Remove empty strings from the result
words = [word for word in words if word]

# Keep track of processed words to avoid duplicates
processed_words = set()

for element in words:
    reversed_element = element[::-1]
    if element not in processed_words and reversed_element in words:
        processed_words.add(element)
        processed_words.add(reversed_element)
        print(element, reversed_element)

        print(f'You healed for {int(number)} hp.')
        print(f'Current health: {initial_health} hp.')