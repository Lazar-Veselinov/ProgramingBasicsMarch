budget = float(input())
n = int(input())
m = int(input())
p = int(input())

price_gpus = 250 * n
price = price_gpus + m * 0.35 * price_gpus + p * 0.1 * price_gpus

if n > m:
    price -= 0.15 * price

if budget >= price:
    print(f"You have {budget - price:.2f} leva left!")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva more!")
