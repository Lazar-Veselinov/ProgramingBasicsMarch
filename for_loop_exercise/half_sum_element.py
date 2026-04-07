from sys import maxsize

n = int(input())
sum = 0
max = -maxsize

for idx in range(n):
    num = int(input())
    if num > max:
        max = num
    sum += num
if max == sum - max:
    print(f"Yes\nSum = {sum - max}")
else:
    print(f"No\nDiff = {abs(sum - 2 * max)}")