stage = input()
ticket_type = input()
num_tickets = int(input())
trophy_photo = input()

price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = num_tickets * 55.5
    elif ticket_type == "Premium":
        price = num_tickets * 105.2
    elif ticket_type == "VIP":
        price = num_tickets * 118.9
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = num_tickets * 75.88
    elif ticket_type == "Premium":
        price = num_tickets * 125.22
    elif ticket_type == "VIP":
        price = num_tickets * 300.4
elif stage == "Final":
    if ticket_type == "Standard":
        price = num_tickets * 110.1
    elif ticket_type == "Premium":
        price = num_tickets * 160.66
    elif ticket_type == "VIP":
        price = num_tickets * 400

free_photos = False

if 4000 >= price > 2500:
    price -= 0.10 * price

elif price > 4000:
    price -= 0.25 * price
    free_photos = True

if trophy_photo == "Y" and not free_photos:
    price += num_tickets * 40

print(f"{price:.2f}")

