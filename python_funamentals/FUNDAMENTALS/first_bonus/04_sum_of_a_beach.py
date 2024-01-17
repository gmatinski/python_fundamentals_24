string = input()
lower_case_string = string.lower()
sun_count = lower_case_string.count("sun")
water_count = lower_case_string.count("water")
fish_count = lower_case_string.count("fish")
sand_count = lower_case_string.count("sand")
total = sun_count + water_count + fish_count + sand_count
print(total)
