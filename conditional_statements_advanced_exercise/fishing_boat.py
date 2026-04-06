budget = int(input())
season = input()
fishermen = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season in ("Summer", "Autumn"):
    price = 4200
elif season == "Winter":
    price = 2600

if fishermen <= 6:
    price -= 0.1 * price
elif 7 <= fishermen <= 11:
    price -= 0.15 * price
else:
    price -= 0.25 * price

if fishermen % 2 == 0 and season != "Autumn":
    price -= 0.05 * price

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
