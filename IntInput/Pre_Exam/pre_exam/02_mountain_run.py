import math

record_in_seconds = float(input())
distance_meters = float(input())
times_in_sec_for_meter = float(input())

seconds_total = distance_meters * times_in_sec_for_meter
slowing = math.floor(distance_meters / 50) * 30  # for every 50m he is slowed with 30 sec
total_time = seconds_total + slowing

if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    total_time -= record_in_seconds
    print(f"No! He was {total_time:.2f} seconds slower.")