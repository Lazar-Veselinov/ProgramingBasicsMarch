import sys

n = int(input())
min = sys.maxsize
max = -sys.maxsize

for n in range(n):
    i = int(input())
    if i > max:
        max = i
    if i < min:
        min = i
print(f"Max number: {max}\nMin number: {min}")