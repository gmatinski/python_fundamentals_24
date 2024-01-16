hour_of_the_exam = int(input())
minute_of_the_exam = int(input())
hour_of_arriving = int(input())
minute_of_arriving = int(input())

time_exam = hour_of_the_exam * 60 + minute_of_the_exam
time_arriving = hour_of_arriving * 60 + minute_of_arriving
diff = abs(time_exam - time_arriving)
hh = diff // 60
mm = diff % 60

if time_exam == time_arriving:
    print("On Time")

if time_arriving < time_exam:
    if diff <= 30:
        print("On Time")
        print(f"{diff} minutes before the start")
    elif 30 < diff <= 59:
        print("Early")
        print(f"{diff} minutes before the start")
    else:
        print("Early")
        print(f"{hh}:{mm:02d} hours before the start")

if time_arriving > time_exam:
    if diff <= 59:
        print("Late")
        print(f"{diff} minutes after the start")
    else:
        print("Late")
        print(f"{hh}:{mm:02d} hours after the start")


