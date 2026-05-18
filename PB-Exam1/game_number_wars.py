player_1 = input()

player_2 = input()

game_finished = False
score = 0
winner = ""
score_1 = 0
score_2 = 0

while True:
    card_1 = input()

    if card_1 == "End of game":
        print(f"{player_1} has "
             f"{score_1} points\n"
             f"{player_2} has "
             f"{score_2} points")

        break

    card_2 = input()

    if card_2 == "End of game":
        print(f"{player_1} has "
             f"{score_1} points\n"
             f"{player_2} has "
             f"{score_2} points")

        break

    if int(card_1) == int(card_2):
        card_1 = input()
        card_2 = input()

        if int(card_1) > int(card_2):
            winner = player_1
            score = score_1

        else:
            winner = player_2
            score = score_2

        print(f"Number wars!\n"
              f"{winner} is winner with "
              f"{score} points")

        game_finished = True

    if game_finished:
        break

    if int(card_1) > int(card_2):
        score_1 += int(card_1) - int(card_2)
    else:
        score_2 += int(card_2) - int(card_1)