animal = input()
my_list = [animal.strip() for animal in animal.split(",")]

if "wolf" in my_list and my_list.count("wolf") == 1:
    if my_list[-1].strip() == "wolf":
        print("Please go away and stop eating my sheep")
    elif "wolf" in my_list:
        reversed_list = my_list[::-1]
        wolf_index = reversed_list.index("wolf")
        print(f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")
