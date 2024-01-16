# невна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# •	Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# •	Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.

travel_km = int(input())
day_night = input()
# taxi no limit
taxi = 0.70  # start tax
bus_limit = 20  # km
train_limit = 100  # km

if travel_km < 20 and day_night == "day":    # taxi
    print(f"{taxi + 0.79 * travel_km:.2f}")
elif travel_km < 20 and day_night == "night":
    print(f"{taxi + 0.90 * travel_km:.2f}")

if 20 <= travel_km < 100:    # bus
    print(f"{0.09 * travel_km:.2f}")
elif travel_km >= 100:
    print(f"{0.06 * travel_km:.2f}")

