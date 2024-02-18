strings = input().split()
search_palindromes = input()
palindromes = []

for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(search_palindromes)} times")