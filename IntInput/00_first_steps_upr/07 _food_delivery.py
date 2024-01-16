# •	Брой пилешки менюта – цяло число в интервала [0 … 99]
# •	Брой менюта с риба – цяло число в интервала [0 … 99]
# •	Брой вегетариански менюта – цяло число в интервала [0 … 99]

# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.


chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

price_chicken = chicken_menu * 10.35
price_fish = fish_menu * 12.40
price_veggie = veggie_menu * 8.15
total = price_chicken + price_fish + price_veggie
dessert = total * (20 / 100)
total_order = total + dessert + 2.50
print(float(total_order))
