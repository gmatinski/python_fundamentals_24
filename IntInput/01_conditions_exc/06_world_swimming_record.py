# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
old_record = float(input())
meters = float(input())
seconds_per_meter = float(input())

time = meters * seconds_per_meter
delay = (meters // 15) * 12.5
his_record = time + delay

if his_record < old_record:
    print(f"Yes, he succeeded! The new world record is {his_record:.2f} seconds.")
else:
    print(f"No, he failed! He was {his_record - old_record:.2f} seconds slower.")
