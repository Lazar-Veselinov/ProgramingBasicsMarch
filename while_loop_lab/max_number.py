from sys import maxsize

command = input()
max = -maxsize

while command != "Stop":
    if int(command) > max:
        max = int(command)

    command = input()

print(max)