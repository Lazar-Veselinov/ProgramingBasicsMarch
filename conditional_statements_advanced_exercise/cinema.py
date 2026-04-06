type = input()
r = int(input())
c = int(input())

winnings = 0

if type == "Premiere":
    winnings =  r * c * 12
elif type == "Normal":
    winnings = r * c * 7.5
elif type == "Discount":
    winnings = r * c * 5

print(f"{winnings:.2f} leva")