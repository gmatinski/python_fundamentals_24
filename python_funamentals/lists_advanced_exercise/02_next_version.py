version = [int(num) for num in input().split(".")]
version[2] += 1

for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1

print(".".join(str(digit) for digit in version))
