trip_price = float(input())
balance = float(input())
days = 0
days_spending = 0
is_enough = False

while days_spending < 5:
    operation = input()
    sum = float(input())

    days += 1

    if operation == "spend":
        days_spending += 1
        balance = balance - sum if balance > sum else 0

    elif operation == "save":
        days_spending = 0
        balance += sum

        if balance >= trip_price:
            is_enough = True
            break

if is_enough:
    print(f"You saved the money for {days} days.")
else:
    print(f"You can't save the money.\n{days}")