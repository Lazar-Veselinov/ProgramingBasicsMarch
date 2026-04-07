from sys import maxsize

command = input()
min = maxsize

while command != "Stop":
    if int(command) < min:
        min = int(command)

    command = input()

print(min)