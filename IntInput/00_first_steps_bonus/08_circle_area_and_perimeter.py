import math

r = float(input())  #radius
d = 2 * r           # diameter
area = math.pi * (r**2)    #01
parameter = math.pi * d    #P

formated_area = "{:.2f}".format(area)
formated_parameter = "{:.2f}".format(parameter)

print(formated_area)
print(formated_parameter)


