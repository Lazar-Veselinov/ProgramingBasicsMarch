nylon_quantity = int(input())
paint_quantity = int(input())
razreditel_quantity = int(input())
working_hours = int(input())

price_nylon = 1.5
price_paint = 14.5
price_razreditel = 5

final_price_bags = 0.40
final_razreditel_price = price_razreditel * razreditel_quantity
final_paint_price = (paint_quantity + 10/100 * paint_quantity) * price_paint
final_nylon_price = price_nylon * (nylon_quantity + 2)

price_materials = final_paint_price + final_nylon_price + final_razreditel_price + final_price_bags

work_price = (30/100 * price_materials) * working_hours

final_price = price_materials + work_price
print(final_price)