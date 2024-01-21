a = int(input())
b = int(input())
old_value_a = a
old_value_b = b

a = b
b = old_value_a

print(f"Before:\na = {old_value_a}\nb = {old_value_b}\nAfter:\na = {a}\nb = {b}")
