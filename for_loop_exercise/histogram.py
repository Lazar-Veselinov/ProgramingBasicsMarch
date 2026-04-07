n = int(input())
number_p1 = 0
number_p2 = 0
number_p3 = 0
number_p4 = 0
number_p5 = 0

for num in range(n):
    num = int(input())
    if num < 200:
        number_p1 += 1
    elif 200 <= num < 400:
        number_p2 += 1
    elif 400 <= num < 600:
        number_p3 += 1
    elif 600 <= num < 800:
        number_p4 += 1
    else:
        number_p5 += 1

p1 = number_p1 / n * 100
p2 = number_p2 / n * 100
p3 = number_p3 / n * 100
p4 = number_p4 / n * 100
p5 = number_p5 / n * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")