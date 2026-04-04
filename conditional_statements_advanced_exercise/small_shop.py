product = input()
city = input()
quantity = float(input())
price = 0

if product == "coffee":
    if city == "Sofia":
        price = quantity * 0.50
    if city == "Plovdiv":
        price = quantity * 0.40
    if city == "Varna":
        price = quantity * 0.45
elif product == "water":
    if city == "Sofia":
        price = quantity * 0.80
    elif city == "Plovdiv":
        price = quantity * 0.70
    elif city == "Varna":
        price = quantity * 0.70
elif product == "beer":
    if city == "Sofia":
        price = quantity * 1.20
    elif city == "Plovdiv":
        price = quantity * 1.15
    elif city == "Varna":
        price = quantity * 1.10
elif product == "sweets":
    if city == "Sofia":
        price = quantity * 1.45
    if city == "Plovdiv":
        price = quantity * 1.30
    if city == "Varna":
        price = quantity * 1.35
elif product == "peanuts":
    if city == "Sofia":
        price = quantity * 1.60
    if city == "Plovdiv":
        price = quantity * 1.50
    if city == "Varna":
        price = quantity * 1.55

print(price)
