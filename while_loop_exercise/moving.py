width = int(input())
length = int(input())
height= int(input())

free_space = width * length * height

n_boxes = 0

result = ""

while free_space > n_boxes:
    command = input()

    if command == "Done":
        result = f"{free_space - n_boxes} Cubic meters left."
        break

    n_boxes += int(command)

else:
    result = (f"No more free space! You need "
              f"{n_boxes-free_space} Cubic meters more.")

print(result)