n1 = int(input())
n2 = int(input())
operator = input()

result = 0
parity = ""

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2

if operator in ("+", "-", "*"):
    if result % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"{n1} {operator} {n2} = {result} - {parity}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")