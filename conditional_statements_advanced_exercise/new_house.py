flower_type = input()
number = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    price = number * 5
    if number > 80:
        price -= 0.1 * price
elif flower_type == "Dahlias":
    price = number * 3.8
    if number > 90:
        price -= 0.15 * price
elif flower_type == "Tulips":
    price = number * 2.8
    if number > 80:
        price -= 0.15 * price
elif flower_type == "Narcissus":
    price = number * 3
    if number < 120:
        price += 0.15 * price
elif flower_type == "Gladiolus":
    price = number * 2.5
    if number < 80:
        price += 0.2 * price

if budget >= price:
    print(f"Hey, you have a great garden with {number} {flower_type} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")

