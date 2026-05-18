from math import floor

num_tournaments = int(input())
starting_points = int(input())
num_won_tournaments = 0
tournament_points = 0

for n in range(num_tournaments):
    reached_stage = input()

    if reached_stage == 'W':
        num_won_tournaments += 1
        tournament_points += 2000

    elif reached_stage == 'F':
        tournament_points += 1200

    elif reached_stage == 'SF':
        tournament_points += 720

average_points = tournament_points / num_tournaments
percent_won_tournaments = num_won_tournaments / num_tournaments * 100
total_points = starting_points + tournament_points

print(f"Final points: {total_points}\n"
      f"Average points: {floor(average_points)}\n"
      f"{percent_won_tournaments:.2f}%")
