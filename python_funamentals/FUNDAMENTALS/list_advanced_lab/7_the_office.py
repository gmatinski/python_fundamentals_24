employee_hap = list(map(int,input().split()))
factor = int(input())

improved_happy = [emp * factor for emp in employee_hap]
rage_happiness = sum(improved_happy) / len(improved_happy)

happy_count = sum(x >= rage_happiness for x in improved_happy)

total_count = len(improved_happy)

if happy_count >= total_count / 2:
    message = "happy"
else:
    message = "not happy"

print(f"Score: {happy_count}/{total_count}. Employees are {message}!")


