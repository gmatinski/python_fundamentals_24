import math

height = int(input())
width = int(input())
percent_not_painted = int(input()) / 100
command = input()


total_surface = height * width * 4
surface_for_painting = total_surface - total_surface * percent_not_painted


while command != "Tired!":
    litters = int(command)
    surface_after_work = surface_for_painting - litters
    surface_for_painting = surface_after_work
    if surface_for_painting < 0:
        print(f"All walls are painted and you have {math.ceil(abs(surface_for_painting))} l paint left!")
        break
    if math.ceil(abs(surface_for_painting == 0)):
        print(f"All walls are painted! Great job, Pesho!")
        break
    command = input()

if command == "Tired!":
    print(f"{math.ceil(surface_for_painting)} quadratic m left.")
