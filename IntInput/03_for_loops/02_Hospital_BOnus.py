period_of_time = int(input())
doctors = 7
treated = 0
untreated = 0

for days in range(1, period_of_time + 1):
    if days % 3 == 0:
        if treated < untreated:
            doctors += 1
    patients = int(input())
    if patients <= 7:
        treated += 1 * patients
    elif patients > 7:
        untreated += (1 * patients) - doctors
        treated += doctors
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
