snowball_quantity = int(input())
value = 0
weight = 0
time = 0
quality = 0
for each_snowball in range(snowball_quantity):
    weight_snowball = int(input())
    time_to_target = int(input())
    quality_of_snowball = int(input())
    snowball_value = int((weight_snowball / time_to_target) ** quality_of_snowball)
    if snowball_value > value:
        value = snowball_value
        weight = weight_snowball
        time = time_to_target
        quality = quality_of_snowball

print(f"{weight} : {time} = {value} ({quality})")


