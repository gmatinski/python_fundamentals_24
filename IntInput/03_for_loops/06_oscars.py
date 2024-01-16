actor_name = input()
points = float(input())
jury = int(input())
total_points = 0

for i in range(jury):
    jury_name = input()
    jury_points_given = float(input())
    total_points = (points + (len(jury_name) * jury_points_given) / 2)
    points = total_points
    if points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points:.1f} more!")

