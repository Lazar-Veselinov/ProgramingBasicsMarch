month = input()
nights = int(input())

price_studio = 0
price_apartment = 0

if month in ("May", "October"):
    price_studio = nights * 50
    price_apartment = nights * 65
    if nights > 14:
        price_studio -= 0.3 * price_studio
    elif 7 < nights <= 14:
        price_studio -= 0.05 * price_studio
elif month in ("June", "September"):
    price_studio = nights * 75.20
    price_apartment = nights * 68.70
    if nights > 14:
        price_studio -= 0.2 * price_studio
elif month in ("July", "August"):
    price_studio = nights * 76
    price_apartment = nights * 77

if nights > 14:
    price_apartment -= 0.1 * price_apartment


print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")