string_of_coins = input()  # [1,3,7,8]
count_of_beggars = int(input()) # 2
list_int_of_coins = [int(coin) for coin in string_of_coins.split(", ")]  # [1,3,7,8]

start_index = 0
final_coins = []
for beggar in range(count_of_beggars):
    beggar_money = 0
    for current_index in range(start_index,len(list_int_of_coins),count_of_beggars):
        beggar_money += list_int_of_coins[current_index]
    final_coins.append(beggar_money)
    start_index += 1

print(final_coins)





