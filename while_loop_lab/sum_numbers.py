number = int(input())
data = int(input())
sum = 0

while True:
    sum += data
    if sum >= number:
        print(sum)
        break
    data = int(input())

