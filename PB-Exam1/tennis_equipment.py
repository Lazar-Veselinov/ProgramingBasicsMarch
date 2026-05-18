from math import floor, ceil

racket_price = float(input())
rackets_number = int(input())
shoes_number = int(input())

shoes_price = 1/6 * racket_price
price = racket_price * rackets_number + shoes_price * shoes_number
equipment_price = 0.2 * price
total_price = price + equipment_price

print(f"Price to be paid by Djokovic "
      f"{floor(1/8 * total_price)}\n"
      f"Price to be paid by sponsors "
      f"{ceil(7/8 * total_price)}")