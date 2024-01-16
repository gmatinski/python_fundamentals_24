w = float(input()) *100 #to cm         # w == lenght of room
h = float(input()) * 100 #to cm      # h == width   #example the room is h = 890cm
3 <= h <= w <= 100         #hallway is 100cm

hall_without_mid = h - 100
desk_h = hall_without_mid // 70
desk_w = w // 120

total_seats = desk_h * desk_w - 3
print(int(total_seats))