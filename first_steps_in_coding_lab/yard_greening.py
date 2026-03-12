square_meters = float(input())
price_square_meter = 7.61
price = square_meters * price_square_meter
final_price = price - 18/100 * price

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {18/100 * price} lv.")