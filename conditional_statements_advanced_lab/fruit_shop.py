fruit = input()
day = input()
quantity = float(input())

if fruit == "banana":
    if day in ["Saturday", "Sunday"]:
        print(f"{quantity * 2.70:.2f}")
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print(f"{quantity * 2.50:.2f}")
    else:
        print("error")
elif fruit == "apple":
    if day in ["Saturday", "Sunday"]:
        print(f"{quantity * 1.25:.2f}")
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print(f"{quantity * 1.20:.2f}")
    else:
        print("error")
elif fruit == "orange":
    if day in ["Saturday", "Sunday"]:
        print(f"{quantity * 0.90:.2f}")
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print(f"{quantity * 0.85:.2f}")
    else:
        print("error")
elif fruit == "grapefruit":
    if day in ["Saturday", "Sunday"]:
        print(f"{quantity * 1.60:.2f}")
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print(f"{quantity * 1.45:.2f}")
    else:
        print("error")
elif fruit == "kiwi":
    if day in ["Saturday", "Sunday"]:
        print(f"{quantity * 3.00:.2f}")
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print(f"{quantity * 2.70:.2f}")
    else:
        print("error")
elif fruit == "pineapple":
    if day in ["Saturday", "Sunday"]:
        print(f"{quantity * 5.60:.2f}")
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print(f"{quantity * 5.50:.2f}")
    else:
        print("error")
elif fruit == "grapes":
    if day in ["Saturday", "Sunday"]:
        print(f"{quantity * 4.20:.2f}")
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print(f"{quantity * 3.85:.2f}")
    else:
        print("error")
else:
    print("error")