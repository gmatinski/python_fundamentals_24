def check_the_rooms(number_of_rooms):
    num_of_free_chairs = 0
    for room in range (1,number_of_rooms +1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
        num_of_free_chairs += difference
    return num_of_free_chairs


count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")