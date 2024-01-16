number = int(input())
sum_of_numbers = 0
boolean = True

while boolean:
    mass_numbers = int(input())
    sum_of_numbers += mass_numbers
    if sum_of_numbers >= number:
        boolean = False
print(sum_of_numbers)