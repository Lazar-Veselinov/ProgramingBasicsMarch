n = int(input())
current = 0
flag = False

for row in range(1, n + 1):

    for column in range(row):
        current += 1
        print(current, end = ' ')

        if current == n:
            flag = True
            break

    if flag:
        break

    print()