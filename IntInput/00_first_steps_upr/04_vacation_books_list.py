num_of_pages = int(input())
read_pages_for_hour = int(input())
days_to_read = int(input())

time_needed = num_of_pages // read_pages_for_hour
time_needed_per_day = time_needed // days_to_read
print(time_needed_per_day)
