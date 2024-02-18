taxed_vehicles = input().split(">>")
tax_family_for_sum = 0
tax_duty_for_sum = 0
tax_sports_for_sum = 0
for element in taxed_vehicles:
    elements = element.split()

    car_type = elements[0]
    year_of_tax = int(elements[1])
    km_traveled = int(elements[2])

    if car_type not in ["family", "heavyDuty", "sports"]:
        print("Invalid car type.")
        continue

    if car_type == "family":
        tax_family = km_traveled // 3000
        total_tax_family = tax_family * 12 + (50 - year_of_tax * 5)
        print(f"A family car will pay {total_tax_family:.2f} euros in taxes.")
        tax_family_for_sum += total_tax_family

    elif car_type == "heavyDuty":
        tax_duty = km_traveled // 9000
        total_tax_duty = tax_duty * 14 + (80 - year_of_tax * 8)
        print(f"A heavyDuty car will pay {total_tax_duty:.2f} euros in taxes.")
        tax_duty_for_sum += total_tax_duty

    elif car_type == "sports":
        tax_sports = km_traveled // 2000
        total_tax_sports = tax_sports * 18 + (100 - year_of_tax * 9)
        print(f"A sports car will pay {total_tax_sports:.2f} euros in taxes.")
        tax_sports_for_sum += total_tax_sports

national_agency = tax_family_for_sum + tax_duty_for_sum + tax_sports_for_sum
print(f"The National Revenue Agency will collect {national_agency:.2f} euros in taxes.")




