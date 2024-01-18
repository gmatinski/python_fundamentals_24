number_of_lines = int(input())
total_water = 0
for liters_of_water in range(number_of_lines):
    poured_water = int(input())
    total_water += poured_water
    if total_water > 255:
        print("Insufficient capacity!")
        total_water -= poured_water
        continue
print(total_water)
