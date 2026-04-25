height = int(input())
weight = int(input())

number_pieces = height * weight

result = None

while number_pieces > 0:
    command = input()

    if command == "STOP":
        result = f"{number_pieces} pieces are left."
        break

    number_pieces -= int(command)

else:
    result = (f"No more cake left! You need "
              f"{abs(number_pieces)} pieces more.")

print(result)