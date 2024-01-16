# •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
mackerel = float(input())  #цена на скумрията на килограм
sprat = float(input())    #цена на цацата на килограм
bonito = float(input())
safrid  = float(input())
mussel = int(input())

bonito_price_per_kg = (mackerel * 0.6) + mackerel  #лв за килограм
bonito_price = bonito * bonito_price_per_kg
safrid_price_per_kg = (sprat * 0.8) + sprat      #лв за килограм
safrid_price = safrid * safrid_price_per_kg
mussel_price_per_kg = 7.50                #лв за килограм
mussel_price = mussel_price_per_kg * mussel

total = bonito_price + safrid_price + mussel_price
format_total = "{:.2f}".format(total)
print(format_total)







