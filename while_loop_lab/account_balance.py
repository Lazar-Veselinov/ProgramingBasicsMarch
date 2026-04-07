command = input()
sum = 0

while command != "NoMoreMoney":

    if float(command) >= 0:
        print(f"Increase: {float(command):.2f}")
        sum += float(command)
    else:
        print("Invalid operation!")
        break

    command = input()

print(f"Total: {sum:.2f}")