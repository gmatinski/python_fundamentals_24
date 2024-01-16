bottles = int(input())  # 750ml
# 5ml dish
# 15ml pot
total_deg = bottles * 750
pots = 0
plates = 0
counter = 1
plates_counter = 0
pots_counter = 0
while bottles > 0:
    dishes = input()
    if dishes.isdigit():
        dishes_to_num = int(dishes)
        if counter % 3 == 0:
            pots_counter += dishes_to_num
            pots = dishes_to_num * 15
            total_deg -= pots
        else:
            plates_counter += dishes_to_num
            plates = dishes_to_num * 5
            total_deg -= plates
        counter += 1
    elif dishes == "End":
        print(
            f"Detergent was enough!\n{plates_counter} dishes and {pots_counter} pots were washed.\nLeftover detergent "
            f"{total_deg} ml.")
        break

    if total_deg < 0:
        print(f"Not enough detergent, {abs(total_deg)} ml. more necessary!")
        break
