days = int(input())
room_type = input()
rating = input()

nights = days - 1
price = 0

if room_type == "room for one person":
    price = nights * 18
elif room_type == "apartment":
    price = nights * 25
    if days < 10:
        price -= 0.3 * price
    elif 10 <= days <= 15:
        price -= 0.35 * price
    else:
        price -= 0.5 * price
elif room_type == "president apartment":
    price = nights * 35
    if days < 10:
        price -= 0.1 * price
    elif 10 <= days <= 15:
        price -= 0.15 * price
    else:
        price -= 0.2 * price

if rating == "positive":
    price += 0.25 * price
elif rating == "negative":
    price -= 0.1 * price

print(f"{price:.2f}")

