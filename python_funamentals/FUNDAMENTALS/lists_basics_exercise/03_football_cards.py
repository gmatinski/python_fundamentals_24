team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ["B-" + str(num) for num in range (1,12)]
end_game = False
card = input().split()

for player in card:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        end_game = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if end_game:
    print("Game was terminated")








