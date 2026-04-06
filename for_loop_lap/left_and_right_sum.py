n = int(input())
left_sum = 0
right_sum = 0

for idx in range(n * 2):
    i = int(input())
    if idx < n:
        left_sum += i
    else:
        right_sum += i

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(right_sum - left_sum)}")