from math import floor

n_tournaments = int(input())
points = int(input())

tournament_points = 0
won_tournaments = 0

for _ in range(n_tournaments):
    reached_stage = input()

    if reached_stage == "W":
        won_tournaments += 1
        tournament_points += 2000
        points += 2000
    elif reached_stage == "F":
        tournament_points += 1200
        points += 1200
    elif reached_stage == "SF":
        tournament_points += 720
        points += 720

average_tournament_points = tournament_points / n_tournaments
won_tournaments_percentage = won_tournaments / n_tournaments * 100

print(f"Final points: {points}\nAverage points: {floor(average_tournament_points)}\n{won_tournaments_percentage:.2f}%")