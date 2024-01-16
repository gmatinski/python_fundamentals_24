length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_of_tank = length * width * height
liters = volume_of_tank / 1000 #Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.
needed_liters_tofill = liters *(1-(percent / 100))

print(needed_liters_tofill)
