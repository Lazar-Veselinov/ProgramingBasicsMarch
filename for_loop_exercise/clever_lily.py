age = int(input())
price_machine = float(input())
price_toy = int(input())

brother_take = 0
birthday_money = 0
saved_money = 0
count_even_birthdays = 0
toy_money = 0

for n in range(1, age + 1):
    if n % 2 != 0:
        toy_money += price_toy
    else:
        count_even_birthdays += 1
        birthday_money += 10 * count_even_birthdays - 1

saved_money = toy_money + birthday_money
if saved_money >= price_machine:
    print(f"Yes! {saved_money - price_machine:.2f}")
else:
    print(f"No! {price_machine - saved_money:.2f}")

