COINS_200 = 200
COINS_100 = 100
COINS_50 = 50
COINS_20 = 20
COINS_10 = 10
COINS_5 = 5
COINS_2 = 2
COINS_1 = 1

change = int(float(input()) * 100)

number_coins = 0

while change:
    if change >= 200:
        change -= COINS_200

    elif change >= 100:
        change -= COINS_100
    elif change >= 50:
        change -= COINS_50
    elif change >= 20:
        change -= COINS_20
    elif change >= 10:
        change -= COINS_10
    elif change >= 5:
        change -= COINS_5
    elif change >= 2:
        change -= COINS_2
    elif change >= 1:
        change -= COINS_1

    number_coins += 1

print(number_coins)