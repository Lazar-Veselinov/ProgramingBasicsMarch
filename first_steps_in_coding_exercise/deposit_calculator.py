deposit = float(input())
time = int(input())
lihven_percent = float(input()) / 100
sum = deposit + time * ((deposit * lihven_percent) / 12)
print(sum)