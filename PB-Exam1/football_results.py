won_games = 0
lost_games = 0
draw_games = 0

for game in range(3):
    game = input()

    if int(game[0]) > int(game[2]):
        won_games += 1
    elif int(game[0]) < int(game[2]):
        lost_games += 1
    else:
        draw_games += 1

print(f"Team won {won_games} games.\n"
      f"Team lost {lost_games} games.\n"
      f"Drawn games: {draw_games}")