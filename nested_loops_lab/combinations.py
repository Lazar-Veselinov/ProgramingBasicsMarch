n = int(input())

equals = 0
for i in range(26):
    for j in range(26):
        for k in range(26):
            if i + j + k == n:
                equals += 1
                break

print(equals)