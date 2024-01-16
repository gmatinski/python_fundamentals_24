width = int(input())
length = int(input())
height = int(input())
space = width * length * height
box_count = 0
while space > 0:   # По добре е да има boxes = input() над while и while да стане : while boxes != "Done"
    boxes = input()
    if boxes.isdigit():
        boxes = int(boxes)
        box_count += boxes
        if box_count >= space:
            print(f"No more free space! You need {box_count - space} Cubic meters more.")
            break
    if boxes == "Done":
        print(f"{abs(box_count - space)} Cubic meters left.")
        break



