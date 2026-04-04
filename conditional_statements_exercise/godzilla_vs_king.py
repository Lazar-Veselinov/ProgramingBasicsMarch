budget = float(input())
people = int(input())
price_clothing_per_artist = float(input())

price_clothing = people * price_clothing_per_artist

if people > 150:
    price_clothing -= 0.1 * price_clothing

decor = 0.1 * budget

if decor + price_clothing > budget:
    print("Not enough money!")
    print(f"Wingard needs {decor + price_clothing - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - decor - price_clothing:.2f} leva left.")
