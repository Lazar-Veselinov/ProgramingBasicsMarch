price_holiday = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

quantity_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks

price = number_bears * 4.1 + number_dolls * 3 + number_puzzles * 2.6 + number_minions * 8.2 + number_trucks * 2

if quantity_toys >= 50:
    price -= 0.25 * price
saved_money = price - 0.1 * price

if saved_money >= price_holiday:
    print(f"Yes! {saved_money - price_holiday:.2f} lv left.")
else:
    print(f"Not enough money! {price_holiday - saved_money:.2f} lv needed.")