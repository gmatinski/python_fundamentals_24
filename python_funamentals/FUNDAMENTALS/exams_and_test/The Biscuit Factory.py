biscuits_per_day_per_worker = int(input())
count_of_workers = int(input())
competing_factory_biscuit = int(input())   # 30 day

total_biscuits_for_the_day = biscuits_per_day_per_worker * count_of_workers
overall_biscuits = 0

for day in range(1,31):
    if day % 3 == 0:
        overall_biscuits += int(total_biscuits_for_the_day * 0.75)
        continue
    overall_biscuits += total_biscuits_for_the_day

print(f"You have produced {overall_biscuits} biscuits for the past month.")
if overall_biscuits > competing_factory_biscuit:
    difference = overall_biscuits - competing_factory_biscuit
    percentage = difference / competing_factory_biscuit * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")

elif competing_factory_biscuit > overall_biscuits:
    difference = competing_factory_biscuit - overall_biscuits
    percentage = difference / competing_factory_biscuit * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")



