lines = int(input())
positive_list = []
negative_list = []

for i in range(lines):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

count_of_pos = len(positive_list)
sum_of_negatives = sum(negative_list)
print(f"{positive_list}\n{negative_list}\nCount of positives: {count_of_pos}\n"
      f"Sum of negatives: {sum_of_negatives}")
