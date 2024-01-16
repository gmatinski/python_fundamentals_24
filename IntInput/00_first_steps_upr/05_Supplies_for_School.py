num_of_pen = int(input())
num_of_markers = int(input())
cleaning_detergent_L = int(input())
discount_perc = int(input()) / 100
pack_pens = 5.80
pack_markers = 7.20
detergent = 1.20

price_of_pens = num_of_pen * pack_pens
price_of_markers = num_of_markers * pack_markers
price_of_detergent = cleaning_detergent_L * detergent
total = price_of_pens + price_of_markers + price_of_detergent

total_with_discount = total - (total * discount_perc )
print(total_with_discount)
