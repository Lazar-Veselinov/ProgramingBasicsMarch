fee = int(input())

shoes_price = fee - 0.4 * fee
clothing_price = shoes_price - 0.2 * shoes_price
ball_price = 1/4 * clothing_price
accessories_price = 1/5 * ball_price

total_spendings = fee + shoes_price + clothing_price + ball_price + accessories_price
print(f"{total_spendings:.2f}")