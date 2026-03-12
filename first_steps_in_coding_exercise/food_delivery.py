n_chicken = int(input())
n_fish = int(input())
n_veg = int(input())

chicken_menu = 10.35
fish_menu = 12.40
veg_menu = 8.15

price = chicken_menu * n_chicken + fish_menu * n_fish + veg_menu * n_veg
desert = 20/100 * price

final_price = price + desert + 2.50
print(final_price)