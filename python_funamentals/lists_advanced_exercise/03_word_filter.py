text = [string for string in input().split()]

for word in text:
    if len(word) % 2 == 0:
        print(word)

# text = input().split()
#
# words = [word for word in text if len(word) % 2 == 0]
# print("\n".join(words))