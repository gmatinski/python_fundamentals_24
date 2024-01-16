# 1.	x – височината на къщата – реално число в интервала [2...100]
# 2.	y – дължината на страничната стена – реално число в интервала [2...100]
# 3.	h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]

x = float(input())  # височината на къщата
y = float(input())  # дължината на страничната стена
h = float(input())  # височината на триъгълната стена на прокрива
door = 1.2 * 2
window = 1.5 * 1.5

side_wall = (x * y) * 2 - (window * 2)
front_wall = (x * x) * 2 - door
wall_total = (side_wall + front_wall) / 3.4  # green
format_wall = "{:.2f}".format(wall_total)

roof_side = (x * y) * 2
roof_front = ((x * h) / 2) * 2
roof_total = (roof_side + roof_front) / 4.3  # red
format_roof = "{:.2f}".format(roof_total)

print(format_wall)
print(format_roof)
