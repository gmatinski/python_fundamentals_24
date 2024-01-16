flowers_type = input()
number_of_flowers = int(input())
budget = int(input())
final_price = 0

if flowers_type == "Roses" and number_of_flowers > 80:
    final_price = (number_of_flowers * 5) - (number_of_flowers * 5) * 0.1
elif flowers_type == "Dahlias" and number_of_flowers > 90:
    final_price = (number_of_flowers * 3.80) - (number_of_flowers * 3.80) * 0.15
elif flowers_type == "Tulips" and number_of_flowers > 80:
    final_price = (number_of_flowers * 2.80) - (number_of_flowers * 2.80) * 0.15
elif flowers_type == "Narcissus" and number_of_flowers < 120:
    final_price = (number_of_flowers * 3) + (number_of_flowers * 3) * 0.15
elif flowers_type == "Gladiolus" and number_of_flowers < 80:
    final_price = (number_of_flowers * 2.50) + (number_of_flowers * 2.50) * 0.2

if flowers_type == "Roses" and number_of_flowers <= 80:
    final_price = number_of_flowers * 5
elif flowers_type == "Dahlias" and number_of_flowers <= 90:
    final_price = number_of_flowers * 3.80
elif flowers_type == "Tulips" and number_of_flowers <= 80:
    final_price = number_of_flowers * 2.80
elif flowers_type == "Narcissus" and number_of_flowers >= 120:
    final_price = number_of_flowers * 3
elif flowers_type == "Gladiolus" and number_of_flowers >= 80:
    final_price = number_of_flowers * 2.50

if budget >= final_price:
    print(
        f"Hey, you have a great garden with {number_of_flowers} {flowers_type} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")