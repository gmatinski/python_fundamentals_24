prime_num = 0
non_prime = 0

command = input()

while command != "stop":
    current_num = int(command)
    if current_num < 0:
        current_num = 0
        print("Number is negative.")
    count = 0
    for i in range(1, current_num + 1):
        if current_num % i == 0:
            count += 1
        if command == "stop":
            break
    if count > 2:
        non_prime += current_num
    else:
        prime_num += current_num
    command = input()
print(f"Sum of all prime numbers is: {prime_num}")
print(f"Sum of all non prime numbers is: {non_prime}")



