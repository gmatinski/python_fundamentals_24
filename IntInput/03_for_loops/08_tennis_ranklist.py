number_of_tournaments = int(input())
starting_points = int(input())
points = 0
total_points = 0
won_tournaments = 0
for i in range(number_of_tournaments):
    type_tournament = input()
    if type_tournament == "W":
        won_tournaments += 1
        points = 2000
        total_points += points
    elif type_tournament == "F":
        points = 1200
        total_points += points
    elif type_tournament == "SF":
        points = 720
        total_points += points
total_points += starting_points
average_points = int((total_points - starting_points) / number_of_tournaments)
percent_won = won_tournaments / number_of_tournaments * 100

print(f"Final points: {total_points} \nAverage points: {average_points}\n{percent_won:.2f}%")


