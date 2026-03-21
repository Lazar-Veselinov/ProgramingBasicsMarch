city = input()
s = float(input())

if 0 <= s <= 500:
    if city == "Sofia":
        print(f"{5 / 100 * s:.2f}")
    elif city == "Varna":
        print(f"{4.5 / 100 * s:.2f}")
    elif city == "Plovdiv":
        print(f"{5.5 / 100 * s:.2f}")
    else:
        print("error")
elif 500 < s <= 1000:
    if city == "Sofia":
        print(f"{7 / 100 * s:.2f}")
    elif city == "Varna":
        print(f"{7.5 / 100 * s:.2f}")
    elif city == "Plovdiv":
        print(f"{8 / 100 * s:.2f}")
    else:
        print("error")
elif 1000 < s <= 10000:
    if city == "Sofia":
        print(f"{8 / 100 * s:.2f}")
    elif city == "Varna":
        print(f"{10 / 100 * s:.2f}")
    elif city == "Plovdiv":
        print(f"{12 / 100 * s:.2f}")
    else:
        print("error")
elif s > 10000:
    if city == "Sofia":
        print(f"{12 / 100 * s:.2f}")
    elif city == "Varna":
        print(f"{13 / 100 * s:.2f}")
    elif city == "Plovdiv":
        print(f"{14.5 / 100 * s:.2f}")
    else:
        print("error")
else:
    print("error")