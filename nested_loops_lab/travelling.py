while True:
    saved_money = 0

    destination = input()

    if destination == "End":
        break

    budget = float(input())

    while saved_money < budget:
        sum = float(input())
        saved_money += sum

    if saved_money >= budget:
        print(f"Going to {destination}!")